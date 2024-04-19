---
title: Stupid Coding Tip
draft: false
tags: 
date: 2024-04-04
linkedin-promo: false
---
It's really important to be able to follow the dimensionality of tensors as they move through a neural network. I love using Visual Studio Code debugging for this. But sometimes running an entire model just to do this debugging piece can be really cumbersome (setting up a bunch of libraries in a conda environment, etc.). And sometimes—as in the case for me today—I can't even fit the model (Mixtral) on my machine.

Here's my stupid tip, which applies if the model code you want to run is relatively decoupled from other dependencies. The idea is obvious enough that any experienced programmer is like 'whatevs', but I've never seen it shown before, so here you go...

I grab the code in question, drop it in a python file (using some generic environment that has torch and transformers), add whatever imports are necessary. Add code to instantiate classes and supply config and inputs. Basically do whatever you need to do to get the code to run.

Here's what this looked like for today's exercise, where I wanted to make sure I could follow what was happening in the MoE-related classes in Mixtral. Here's the relevant code, pasted straight out of [HuggingFace](https://github.com/huggingface/transformers/blob/v4.39.3/src/transformers/models/mixtral/modeling_mixtral.py) (the details aren't important, but I'm putting it all here for reference):

```python
class MixtralBLockSparseTop2MLP(nn.Module):
    def __init__(self, config: MixtralConfig):
        super().__init__()
        self.ffn_dim = config.intermediate_size
        self.hidden_dim = config.hidden_size

        self.w1 = nn.Linear(self.hidden_dim, self.ffn_dim, bias=False)
        self.w2 = nn.Linear(self.ffn_dim, self.hidden_dim, bias=False)
        self.w3 = nn.Linear(self.hidden_dim, self.ffn_dim, bias=False)

        self.act_fn = ACT2FN[config.hidden_act]

    def forward(self, hidden_states):
        current_hidden_states = self.act_fn(self.w1(hidden_states)) * self.w3(hidden_states)
        current_hidden_states = self.w2(current_hidden_states)
        return current_hidden_states


class MixtralSparseMoeBlock(nn.Module):
    """
    This implementation is
    strictly equivalent to standard MoE with full capacity (no
    dropped tokens). It's faster since it formulates MoE operations
    in terms of block-sparse operations to accomodate imbalanced
    assignments of tokens to experts, whereas standard MoE either
    (1) drop tokens at the cost of reduced performance or (2) set
    capacity factor to number of experts and thus waste computation
    and memory on padding.
    """

    def __init__(self, config):
        super().__init__()
        self.hidden_dim = config.hidden_size
        self.ffn_dim = config.intermediate_size
        self.num_experts = config.num_local_experts
        self.top_k = config.num_experts_per_tok

        # gating
        self.gate = nn.Linear(self.hidden_dim, self.num_experts, bias=False)

        self.experts = nn.ModuleList([MixtralBLockSparseTop2MLP(config) for _ in range(self.num_experts)])

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        """ """
        batch_size, sequence_length, hidden_dim = hidden_states.shape
        hidden_states = hidden_states.view(-1, hidden_dim)
        # router_logits: (batch * sequence_length, n_experts)
        router_logits = self.gate(hidden_states)

        routing_weights = F.softmax(router_logits, dim=1, dtype=torch.float)
        routing_weights, selected_experts = torch.topk(routing_weights, self.top_k, dim=-1)
        routing_weights /= routing_weights.sum(dim=-1, keepdim=True)
        # we cast back to the input dtype
        routing_weights = routing_weights.to(hidden_states.dtype)

        final_hidden_states = torch.zeros(
            (batch_size * sequence_length, hidden_dim), dtype=hidden_states.dtype, device=hidden_states.device
        )

        # One hot encode the selected experts to create an expert mask
        # this will be used to easily index which expert is going to be sollicitated
        expert_mask = torch.nn.functional.one_hot(selected_experts, num_classes=self.num_experts).permute(2, 1, 0)

        # Loop over all available experts in the model and perform the computation on each expert
        for expert_idx in range(self.num_experts):
            expert_layer = self.experts[expert_idx]
            idx, top_x = torch.where(expert_mask[expert_idx])

            if top_x.shape[0] == 0:
                continue

            # in torch it is faster to index using lists than torch tensors
            top_x_list = top_x.tolist()
            idx_list = idx.tolist()

            # Index the correct hidden states and compute the expert hidden state for
            # the current expert. We need to make sure to multiply the output hidden
            # states by `routing_weights` on the corresponding tokens (top-1 and top-2)
            current_state = hidden_states[None, top_x_list].reshape(-1, hidden_dim)
            current_hidden_states = expert_layer(current_state) * routing_weights[top_x_list, idx_list, None]

            # However `index_add_` only support torch tensors for indexing so we'll use
            # the `top_x` tensor here.
            final_hidden_states.index_add_(0, top_x, current_hidden_states.to(hidden_states.dtype))
        final_hidden_states = final_hidden_states.reshape(batch_size, sequence_length, hidden_dim)
        return final_hidden_states, router_logits
```

In order to get it running in a standalone file, I had to make the following additions (here you are guided by the missing dependencies and vars highlighted in VS Code):

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class FakeConfig:
	def __init__(
		self,
		hidden_size=4096,
		intermediate_size=14336,
		hidden_act=nn.SiLU(),
		num_experts_per_tok=2,
		num_local_experts=8
	):
		self.hidden_size = hidden_size
		self.intermediate_size = intermediate_size
		self.hidden_act = hidden_act
		self.num_experts_per_tok = num_experts_per_tok
		self.num_local_experts = num_local_experts

# Insert classes above...

moe_config = FakeConfig()
moe_block = MixtralSparseMoeBlock(moe_config)

input = torch.randn((2, 512, 4096))
final_hidden_states, router_logits = moe_block(input)
```

and change two lines in the original snippet:

```python
	# def __init__(self, config: MixtralConfig):
	def __init__(self, config: FakeConfig):

# ...

	# self.act_fn = ACT2FN[config.hidden_act]
	self.act_fn = config.hidden_act
```

That was quick and easy, and now I can step through the code. We're off to the races!
