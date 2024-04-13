---
title: Reservoir Computing
draft: true
tags: 
date:
---
Sometime around the summer of 2021 I came across the paper [Pretrained Transformers as Universal Computation Engines](https://arxiv.org/abs/2103.05247) (Lu et al., 2021), and was blown away. In this paper they took a GPT-2 pretrained as a language model, then froze the self attention and feed forward parameters (keeping the embedding / output layer and layer norm params trainable). The learned parameters accounted for well under 1% of the total model params.

They proceeded to retrain this mostly-frozen model on several very different tasks like bit operations, image classification, and protein folding predictions. Amazingly, the mostly-frozen GPT performed about as well as one trained from scratch on the test tasks.

The idea that one could take a model pretrained on natural language and then, by retraining such a small fraction of the parameters, have it perform well on seemingly unrelated tasks seemed absolutely crazy.

Then a while later I encountered another (#decoder-only? or BERT-style??#) paper (which had come out about the same time): [FNet](https://arxiv.org/abs/2105.03824) (Lee-Thorp et al., 2022).[^1] Here the idea is that they replace the self-attention layers with unlearned linear transformations that mix information across tokens in the input sequence. In other words, there was no directly learned self-attention mechanism, just a sort of channel mixing that the model needed to learn how to make use of (via (#layer norm??#))

(#trained / tested on what?#)

FNet didn't outperform vanilla transformers, but it came close, and used less compute.

I think of both of these concepts as providing a 'fixed computation' substrate surrounded by trainable components that can learn to make use of the computation. In an abuse of terminology, I refer to them as forms of reservoir computing.[^2]



(#Exciting because they offer a route to do more with less#)


[^1]:  Another paper in a similar vein is [MLP-Mixer](https://arxiv.org/abs/2105.01601) (Tolstikhin et al., 2021). Here the proposal was to replace the self-attention layers with MLPs that—instead of operating within each token's stream—were 'rotated' and operated across tokens. (##)

[^2]: Technically reservoir computing refers to the use of a fixed recurrent network to process sequential data, with only the output layer trained. Is there a better term?