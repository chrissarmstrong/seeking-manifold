---
title: The Vision System
draft: true
tags: 
date: 2024-03-18
---
In late 2022 I began to recognize that we should really be looking to biological systems for clues about how evolution has already solved for intelligent systems (to which a reasonable reaction would be "Duh!"). After a few months learning a bit about neuroscience[^1], one of the subjects I got very interested in is the vision system (in humans and other mammals, primarily).

## The ventral / dorsal split

The human vision system has a functional split between two streams of information, the ventral stream and the dorsal stream. The ventral stream is sometimes called the 'what' stream, as it seems to be geared towards recognition and identification of objects, while the dorsal stream is sometimes called the 'where' stream, as it seems to be geared towards spatial awareness and detection of motion.

There is evidence that this split also exists in other species, from mammals (rats, cats, other primates) and also in birds and reptiles. This hints that the split may perform some rather basic function.

It could certainly be a an efficiency enhancement, allowing the vision system to get by with less bandwidth between the eyes and the rest of the brain. But could it be somehow more fundamental?

What does the split mean for the overall performance of the system (for example, does it allow better object detection than a single stream would)? Does it somehow force a better representation?

There has been work trying to apply learnings from the split stream. For example, Patrick Mineault and collaborators have done [some interesting](https://your-head-is-there-to-move-you-around.netlify.app/) [and clever experiments](https://ventral-dorsal-model.netlify.app/). But in general it seems like an under-researched area in terms of its importance to artificial systems.

I also am a big believer in Yann LeCun's point of view that we should be focusing on working in the representation space (as opposed to, say, pixel space in the case of images or video). His work on JEPA-type systems is a natural outgrowth of that belief. An idea that has occurred to me more recently - after listening to [Yann's latest interview with Lex Fridman](https://www.youtube.com/watch?v=5t1vTLU7s40) - is whether the ventral / dorsal split could be helping to prevent collapse in a JEPA-like biological system? In other words, could nature have arrived at this two-stream mechanism as a way of regularizing a JEPA-like system?

## Eye movement and the fovea

The human fovea feeds high-resolution but very narrow field of view information to both the ventral and dorsal streams, but seems to be more important to the former.

The eye has a number of different mechanisms related to motion. Some, like vergence movements (two eyes focusing on a single object to maintain binocular vision) and reflexive movements (eyes moving to maintain a fixed point of focus while the head / body moves) have a purpose that seems pretty straightforward. Saccades, which are the rapid movements of the eye from one spot to another, I find more interesting.

One set of ideas that has been swirling in my head since then relates to whether an architecture similar to our vision system could help artificial systems learn better representations. For example:
- Is the way our eyes move somehow critical to allow recognition of parts and assembling them into a whole?
- Are eye saccades somehow key to the learning process? For example, do they provide a contrastive signal to the system (for example, as discussed in [the CLAPP paper](https://arxiv.org/abs/2010.08262) by Illing et al.)? Do they afford some sort of attentional or energy efficiency?
- It's interesting to think about how eye motion may play into the concept of 'fast weights' in a system. I believe Geoff Hinton and collaborators have talked about this.
- How does [visual 'crowding'](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2772078/) fit into the picture? This effect seems like the byproduct of some mechanism, but is it important in some way?

## Interaction with the 3D world

Geoff Hinton has long argued that we should be paying close attention to evidence from human perception, as it contains clues that are valuable for designing artificial NNs.[^2] He often points to his ['cube on a corner' demonstration](https://www.cs.toronto.edu/~hinton/absps/cube.pdf) as evidence that humans have built-in mechanisms to handle 3D symmetries, and that this has implications for how we perceive the world and how we learn. Jeff Hawkins has 



(#Hinton's capsules#)

(#causality#)

(#simulation#)

(#tie to experiments done so far#)


[^1]: [Insights from the Brain](https://www.insightsfromthebrain.com/), by Matthieu Thiboust, is a great place to start
[^2]: As have others, like Ray Kurzweil in *How to Create a Mind* and Jeff Hawkins in *A Thousand Brains* (although their views do not totally align on the details!).