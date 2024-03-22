---
title: CIFAR for Video (Towards Simulated Environments for Self-Supervised Learning)
draft: false
tags: 
date: 2024-03-17
---
I believe that if we want to have systems that truly learn causality it will help enormously, and may be crucial, to have a visual understanding of the 3D, physical world. When I started thinking about video experiments that could take cues from [[The Vision System|the human vision system]], one of the first things I did was to try to find the video analog of [the CIFAR dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

This would be a dataset of simple videos, available at low resolutions, and would feature motion (and maybe audio?) of inanimate (and maybe animate) objects interacting in physically-realistic ways.

From what I can tell, such a dataset doesn't exist.

But as I started thinking more about what I wanted for my experimentation, it seemed likely that - even if I found something that purported to be a 'CIFAR for video' - it probably wouldn't do *everything* I wanted.

I want to have videos in different categories that I could use in curriculum-based training of models. Imagine starting to train a model with very basic shapes in a spartan space (a mostly empty room) with rudimentary motion. You use this environment to see if you can get a model to understand some basic physics concepts, like visual occlusion, two objects making contact, stability, gravity, etc.

>[!Note]
> [[Measuring Success of Self-Supervised Systems|How you measure success]] in such a system is an interesting topic in itself. And doing that may be aided by the availability of unlikely or 'impossible' scenarios.

Assuming you can get a model to gain an understanding of rudimentary worlds, then you begin adding in various forms of complexity and realism: more complex shapes, non-rigid shapes, transparency, different types of motion, animated (self-locomoting) objects, etc. There are multiple classes of things that you could do to make the simplest scenarios more realistic.

All of that would be for self-supervised training of systems. Then you'd want the ability to also generate labeled datasets: classification, object detection, segmentation, depth map, etc.

Here's a diagram I threw together while brainstorming about this:

![[Pasted image 20240321182001.png]]

Training a model with a progressive curriculum like this would require the ability to generate a lot of scenes, with control over these different components.

After resigning myself to the fact that there's nothing that fits this bill off-the-shelf, I started looking at packages that would let me roll my own. I landed on [TDW](https://www.threedworld.org/). It is feature-rich, very powerful, actively maintained, nicely documented, open source, and very much geared towards this sort of task (as opposed to, say, gaming).

I've just started playing with this idea in my spare time. The longer-term goal is to procedurally generate scenes based on some of the criteria above so that you can run a model through a curriculum. Here's a snippet of one generated scene with no audio, static assets in a bare room, and a kind of random observer motion that would potentially allow a system to learn about viewer perspectives, occlusion, and the like:

![[tdw-sample.mp4]]

Building this into a little framework seems like a useful project, but not something I've had the time to do. More to come, I hope!

Here are some semi-related references that got me thinking about why we may want to train a model in this way:
- [The Development of Embodied Cognition: Six Lessons from Babies](https://www.semanticscholar.org/paper/The-Development-of-Embodied-Cognition%3A-Six-Lessons-Smith-Gasser/25f8e9e35cafd7fb686d939f274111bcffeafd6b), Smith and Gasser, 2005. This is a really cool read about the development of babies (mostly human, but touching on other animals as well).
- [Building Machines That Learn and Think Like People](https://arxiv.org/abs/1604.00289), Lake et al., 2016. Josh Tenenbaum and collaborators have long been advocating for systems that go beyond pattern recognition towards an actual understanding of causality. Here's [a more recent talk by Josh](https://www.youtube.com/watch?v=gzaIrD3jki8) (at the Santa Fe Institute, 2023)
- Here's [a very good talk by LeCun](https://www.youtube.com/watch?v=_JfEScYyVCE) (at that same Santa Fe Institute conference, 2023)
