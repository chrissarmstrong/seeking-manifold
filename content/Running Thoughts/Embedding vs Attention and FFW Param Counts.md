---
title: Embedding vs Attention and FFW Param Counts
draft: false
tags: 
date: 2023-12-17
---
Sometimes getting into the weeds of an experiment makes dead-obvious facts hit you in the head so hard you feel like a dummy. That happened to me when pondering the results of the [[Residual Stream Data Lane]] experiments.

In particular, I'd been chasing something that is just not that important in many contexts. The relative parameter counts of the embedding vs the self-attention and feedforward layers of a transformer depend dramatically on the size and details of the network.
 ![[llm-params-gpt2-vs-llama7b.png]]

The left side of this figure shows the parameter count of a GPT2-scale model (with 124M params, 12 layers, $d_{model}=768$). The token embeddings account for *over 30% of the total parameters*. Hey, I'd been thinking, let's figure a way to reduce that parameter count.

The right side shows the same for a 7B-scale LLM (with 6.7B params, 32 layers, $d_{model}=4096$). In this case, the token embeddings account for *only 3% of the total params*.

So chasing a way to shrink embedding sizes is just not super important when you are using these larger models!
