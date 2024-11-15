---
title: Residual Stream (??)
draft: false
tags: 
date: 2024-11-09
promo-linkedin:
---
Terminology nitpick / question here.

First a quick bit of history, as I understand it: back in 2015, [the original Resnet paper](https://arxiv.org/abs/1512.03385) (He et al., 2015) added a skip connection to the CNN architecture (colored annotations are mine):

![[Resnet-figure-annotated.png]]

The idea was that you would be modeling the output of a layer as the sum of the input $\mathbf{x}$ and some function $\mathcal{F}(\mathbf{x})$, in the hope that it might be easier for the network to learn this little bit $\mathcal{F}(\mathbf{x})$ *added* to the input than it would be to learn the output signal in the absence of any reference at all. They called $\mathcal{F}(\mathbf{x})$ the *residual function* (hence the name Resnet, for residual network).

Nowadays, many transformer-based papers—especially ones in the mechanistic interpretability domain—use the terminology *residual stream* to denote the information that flows layer-wise along the transformer outside of the attention and MLP / FFW components. Here, for example, is an image from the [Mathematical Framework for Transformer Circuits paper](https://transformer-circuits.pub/2021/framework/index.html) by Elhage et al. (the wonderful Anthropic mech int team):

![[transformer-residual-stream.png]]

As indicated in that figure, the residual stream encompasses both the inter-layer piece and the 'skip connection' part where you bypass the attention and MLP / FFW components within an individual layer. In other words, the residual stream does *not* include the part that I would describe as the residual!

I'm curious whether anyone is aware of a reason for this seemingly inconsistent terminology, and where the more recent transformer-based term originated (was it Olah's team at Anthropic?). Reach out if you have any insight.