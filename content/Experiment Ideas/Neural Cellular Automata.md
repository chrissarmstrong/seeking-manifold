---
title: Neural Cellular Automata
draft: false
tags:
  - post/idea
date: 2024-07-05
linkedin-promo: false
---
Recently I came across this great post published a few years ago in Distill: [Growing Neural Cellular Automata](https://distill.pub/2020/growing-ca/), or NCA.

A cellular automata is a cell on a grid that has a set of rules that defines what happens to it based on what its neighboring cells do. *Neural* cellular automata extend that idea by giving each cell an identical neural network and then training that shared network with some objective function.

You can get the flavor of what they're able to do just by looking through their animations showing the images they produce.

I find this fascinating on several fronts:
- The idea that you can have cells that contains a single, shared program to create an entire 'organism' is pretty amazing.
- The creation of the entire organism based on each cell only getting direct information about the state of its immediate neighbors is intriguing.

To reiterate: every one of the cells in these automata has *the exact same set of parameters* (~8k); it is just their *activations* that differ, by virtue of what they see their neighbors doing.

I did a relatively quick (quick for *me*, lol) exercise to re-implement the NCA mechanism in that post. I wanted to do this because 1) I figured it would be a good coding exercise, and 2) I wanted something to use for some exploration (more below). I allowed myself to consult the post, but not the Colab implementation they linked to.

Here's what I've done so far:

I have a simple setup that will train an NCA for either a 28 x 28 image that you draw (using a simple Tk interface) or for an MNIST image. The setup is pretty much what the post outlines for their initial Experiment 1. My neural net is identical to theirs, but I'm using slightly smaller images.

I provide a single-pixel starting point (checkerboard indicates that the $\alpha$ channel is zero): 

![[nca-starting-pixel.png]]

Together with a target image (in this case, my crudely-drawn spotted gecko):

![[gecko-target.png]]

And then we run the training. The are two loops here: an outer loop (over 'training steps') and an inner loop (over 'CA training steps'). The outer loop is typically 800 - 1200 training steps. Each of these training steps consists of a random number of CA training steps (the inner loop) in the range \[64, 96\].[^1]

Within a training step we use backprop through time (BPTT) for that entire set of CA steps. Random masking is applied to the update grid at each CA step.

Batches of 64 images fit in my GPU. Each of the 64 examples has the same starting pixel, the same target, and the same number of CA steps, but they evolve differently because the random update masking is unique for each image in the batch.

Here's a pic showing a training run. The rows are at 400, 800, and 1200 training steps. Each row shows the target image, one of the batch of current output images, and the R/G/B/$\alpha$ channels for that output image.

![[nca-training.png]]

You can see that by 1200 steps (which takes ~7 min on my GPU) the output is looking quite good.

Here's the loss for each batch of images at the end of each training step.

![[nca-training-loss.png]]

I have not yet done any work to stabilize the endpoint or to support regeneration (Experiments 2 and 3 in the post).

Now that we have a trained network, we can use it for inference. We get a gecko going with one pixel and watch it evolve for an arbitrary number of steps. Here we're letting it evolve for 400 steps (so well beyond the max 96 steps it saw during training):

![[animation-gecko.mp4]]

You can see that at times it displays a bit of instability, but given that I did not do anything to provide a stable attractor, not bad at all.

I have some experiments in mind that will require a larger data set to work with, so I instrumented my setup to also be able to use MNIST images for NCA generation.

The only things worth mentioning on the MNIST side are:
1. I did the most hacky thing possible, which is to simply create RGB versions of the grayscale images for training. I could have gained some efficiency my modifying the network to handle grayscale directly (so training only one layer instead of three).
2. There's no true $\alpha$ channel here.

Here's an MNIST example (target on the left, output of the NCA after 800 training steps):

![[mnist-sample.png]]

Here's 400 frames of inference for that NCA (showing noticeably more degradation at the end due to unstable attractor):

![[animation-mnist.mp4]]

## What now?

I know that the entire point of neural cellular automata is to be a little model of life, but *isn't this just a really cool little model of life?* A collection of one type of cell, replicated and interacting only with its next-door neighbors, able to organize themselves into something at a macro scale—wow!

All of this has some ideas bubbling around in my head:
- Could you get a single cell type to generate conditionally? In other words, given some signal from a centralized source to each cell that indicates (for example) 'gecko' or 'snail' or 'bird', could you then control the end result of the generation for those cells? Certainly seems straightforward.
- Could you train the network such that you start with multiple seed pixels and when the different growths meet, they merge into a unit as if from the same seed? This seems somewhat straightforward, similar in nature to the 'stable attractor' concept in the original post.
- Could you organize cells in a hierarchy, such that you have a collection of parts that 'cooperate' to become a well-formed higher-level 'organism'?
- Could you train cells to generate with a target that varies with time? A walking gecko, for example? I really like this idea, but it's not yet clear to me how you do this.
- *Could you use the weights of the learned network as representations of the thing in another network?*

That last idea is one I'm most interested in, and have been thinking about a lot for a few weeks. Here's what has me excited: The fact that the cells are uniform and interact locally is highly reminiscent of [the minicolumn structure found throughout the neocortex](https://en.wikipedia.org/wiki/Cortical_minicolumn).[^2][^3]

Not only that, but the weights encapsulate a time-based aspect of behavior. Readers of this blog may know that I'm really interested in [[Time as a First-Class Citizen]].

You can imagine a scenario where there is a wake / sleep cycle in which the weights of the network are updated during sleep to account for the day's activities and observations. Then these weights form the basis of representations (in both space and time) that are subsequently used in the brain's world model.

Finally, the NCAs are inherently generative. As I discussed in [[Evaluating Representations from Self-Supervised Systems|this post]], I believe that generative capabilities are likely an intrinsic part of our brain.

Repo: (#to do#)

[^1]: The inner loop corresponds to the 'Single update step' figure in the Distill post, the outer loop to the 'Training regime' figure.

[^2]: The minicolumns in the brain don't just have local interactions, hence my thinking also about central signalling and hierarchy.

[^3]: The NCAs are also somehow reminiscent of Hinton's capsule idea, but that analogy isn't yet well formed for me.