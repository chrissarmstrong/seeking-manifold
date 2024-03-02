---
title: Virtual Layer Stacking
draft: false
tags:
---
2024-02
Repo: (#to do#)

## The Idea

There have been indications recently that we can expand the capacity of LLMs by duplicating blocks (and then following up with some sort of fine-tuning). Two examples:
1. [Goliath-120B](https://www.reddit.com/r/LocalLLaMA/comments/17rsmox/goliath120b_quants_and_future_plans/), in which layers from two separate fine-tunes of the same 70B model were interwoven to achieve a much larger model that (at least anecdotally) has very good performance.
2. [Solar 10.7B](https://arxiv.org/pdf/2312.15166.pdf), in which the final 24 (of 32) layers of a pretrained 7B model were slapped onto the initial 24 layers of the same model (so taking the total number of layers from 32 to 48), then the whole thing fine-tuned (they call this *depth upscaling*) to achieve very good performance.

I'm very interested in improving models for low-resource scenarios, and the thought that occurred to me was: could we use *virtual* (that is, weight-tied) layers, each with LoRA-type adapters, to get significantly more layers (hence capability) out of a transformer with a lower parameter count (so less memory during inference) than simply increasing the number of layers?

Note that this wouldn't do *much* to reduce VRAM required for training, since that is dominated by other considerations (#link to note with graphic#). Nor would it help with inference latency or throughput, since you are still walking through all the layers in the forward pass. But if it would help me fit a more capable model onto my little GPU, then that would be a step in the right direction! (Then separately you could look at introducing, say, MoE to reduce latency.)

Here's a diagram of what I did (although it shows a toy two-layer model just to convey the concept):

![[Pasted image 20240302101356.png]]

As indicated in the figure, I ended up adding LoRA (or IA3) adapters to both the 'virtual' (weight-tied) as well as the 'real' layers.

## The Experiment

I did this work using the fully-trained (not by me) [TinyStories-33M model](https://huggingface.co/roneneldan/TinyStories-33M). I grabbed a subset of [this version](https://huggingface.co/datasets/skeskinen/TinyStories-GPT4) of the TinyStories dataset to check perplexity out of the box. PPL = 4.41.

The first thing I was curious about, as a sort of pre-experiment: when you choose to copy real layers to virtual layers (see diagram above), what effect does the mapping from source model to target model have?

Below is a plot showing the results of a few experiments taking the 4-layer fully-trained TinyStories model and duplicating layers so that it is an 8-layer model. No fine tuning is done here.

Each row in the heatmap is a separate experiment, with resulting perplexity on the right. The row in the heatmap shows which of the four layers (0 - 3) of the original model was used for the eight layers (0 - 7) of the new model. For example, the top row shows that constructing the (8-layer) target model using layers [0, 1, 2, 3, 0, 1, 2, 3] from the (4-layer) source model resulted in a perplexity of 8.84.

So one interesting observation (perhaps not surprising) is that none of these mappings result in an 8-layer model that does *better* than the original 4-layer model. At this point, however, we have not applied any LoRA adapters, nor have we done any fine-tuning. We're just gluing together layers as they were originally trained.

Another thing to note is that here I only tried mappings in which you keep the first and last layers in place. I did a little bit of testing where that rule was not respected, and it generally resulted in poorer perplexity.

![[Pasted image 20240302101626.png]]

(narrow down to one option for further testing. Used row 2)

In all runs, froze the main layer matrices and trained only the LoRA (or IA3) matrices (per the first figure above).

(# does this apply here?: Since I'm training for only one epoch I can use the final training loss as a reasonable evaluation metric.#)

## Results

I'm *re-training* on a 250k subset of the dataset that the model saw in pretraining; in retrospect not the best idea.

I'm showing the training curves here (instead of end results) because in some cases when it became clear where the run was trending I got impatient and cut it short.

In this graph, (##)

![[Pasted image 20240302105205.png]]

Notation for the different runs (*TS-33M* refers to the base TinyStories-33M model):
- *TS-33M-8RL-LoRA-Exp1* (brown): 8 'real' layers, with LoRA, with source-to-target mapping of [0, 1, 1, 1, 2, 2, 2, 3]. In other words, I simply *copied* the four new layers from the original 4-layer model (as opposed to using weight tying), then trained some more (with base layers frozen, LoRA updates only). Consider this the baseline. The mix of 4 real + 4 virtual layers was very close to this baseline, as expected.
- *TS-33M-12RVL-LoRA-Exp3* (purple): 6 'real' layers + 6 'virtual' layers, all with LoRA.
- *TS-33M-12RVL-IA3-Exp4* (dark green): 6 'real' layers + 6 'virtual' layers, all with IA3 adapters. Here the IA3 
- *TS-33M-12RVL-IA3-Exp5* (): 

## Takeaways


## Additional Thoughts

I consider this a work in progress that I really want to get back to. I've been a bit surprised - and very bummed - about the results here so far, but I think there is something worth pursuing here, and I want to try out some more ideas.