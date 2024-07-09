---
title: The Vision System
draft: false
tags:
  - post/idea
date: 2024-04-01
promo-linkedin:
---
In late 2022 I began to think that we should really be looking to biological systems for clues about how evolution has solved for intelligent systems (to which a reasonable reaction would be "Duh!"). After a few months learning a bit about neuroscience[^1], one of the subjects I got very interested in is the vision system (in humans and other mammals, primarily).

## The ventral / dorsal split

The human vision system has a functional split between two streams of information, the ventral stream and the dorsal stream. The ventral stream is sometimes called the 'what' stream, as it is geared towards recognition and identification of objects, while the dorsal stream is sometimes called the 'where' stream, and helps with spatial awareness and detection of motion.

There is evidence that this split also exists in other species, from mammals (rats, cats, other primates) and also in birds and reptiles. This hints that the split may perform some rather basic function. It could certainly be a an efficiency enhancement, allowing the vision system to get by with less bandwidth between the eyes and the rest of the brain. But could it be somehow more fundamental?

There has been work trying to apply learnings from the split visual stream. For example, Patrick Mineault and collaborators have done [some interesting](https://your-head-is-there-to-move-you-around.netlify.app/) [and clever experiments](https://ventral-dorsal-model.netlify.app/). But in general it seems like an under-researched area in terms of its importance to AI systems.

I also am a big believer in Yann LeCun's point of view that we should be focusing on working in the representation space (as opposed to, say, pixel space in the case of images or video). His work on JEPA-type systems is a natural outgrowth of that belief. An idea that has occurred to me recently (after listening to [Yann's latest interview with Lex Fridman](https://www.youtube.com/watch?v=5t1vTLU7s40)) is whether evolution might have arrived at this two-stream mechanism as a way to prevent collapse in a JEPA-like biological system? That would be interesting to look into.

## Eye movement and the fovea

The human fovea feeds high-resolution but very narrow field of view information to both the ventral and dorsal streams, but seems to be more important to the former.

The eye has a number of different mechanisms related to motion. Some, like vergence movements (two eyes focusing on a single object to maintain binocular vision) and reflexive movements (eyes moving to maintain a fixed point of focus while the head / body moves) have a purpose that seems pretty straightforward. Saccades, which are the rapid movements of the eye from one spot to another, I find more interesting.

## Interaction with the 3D world

Geoffrey Hinton has long argued that we should be paying close attention to evidence from human perception, as it contains clues that are valuable for designing artificial NNs.[^2] He has often pointed to his ['cube on a corner' demonstration](https://www.cs.toronto.edu/~hinton/absps/cube.pdf) as evidence that humans have built-in mechanisms to handle 3D symmetries, and that this has implications for how we perceive the world and how we learn.

Hinton and colleagues worked for years on ideas related to this. The series of papers related to his 'capsule' concepts are a good resource.

## Related ideas

Here is a quick sampling of ideas related to the above that have been swirling in my head:
- Does the split visual stream allow better object detection than a single stream would? Or does it somehow allow a better internal representation of the world?
- Are eye saccades somehow critical to allow recognition of parts and assembling them into a whole?
- Are eye saccades somehow key to the learning process in the visual system? For example, do they provide a contrastive signal to the system (for example, as discussed in [the CLAPP paper](https://arxiv.org/abs/2010.08262) by Illing et al.)? Do they afford some sort of attentional or energy efficiency? (Related: [[Streaming Data Augmentation?]])
- How does [visual 'crowding'](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2772078/) fit into the picture? This effect seems like a shortcoming or side effect of our vision system, but is it important in some way?
- Could eye motion play into the concept of 'fast weights' in a system? Hinton touched on fast weights briefly at the end of his [Turing Award acceptance speech](https://www.youtube.com/live/VsnQf7exv5I?si=qziCSCKyerZ3JNNW&t=2375) (though his focus there was not vision-related).

All of this to say: it seems like there is an entire research program out there for a group that wants to undertake it! I've started to [[CIFAR for Video|dabble just a bit]].


[^1]: [Insights from the Brain](https://www.insightsfromthebrain.com/), by Matthieu Thiboust, is a great place to start
[^2]: As have others, like Ray Kurzweil in *How to Create a Mind* and Jeff Hawkins in *A Thousand Brains* (although their views do not totally align on the details!).