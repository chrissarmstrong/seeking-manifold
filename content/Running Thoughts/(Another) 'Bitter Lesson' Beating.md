---
title: (Another) 'Bitter Lesson' Beating
draft: false
tags:
  - post/thought
date: 2024-02-26
linkedin-promo: false
---
I keep getting beat over the head with [Sutton's Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf).

My inclination is to always want to cleverly design a system that can do what I think it should do. In the bitter lesson world we know how that tends to turn out.

Instead I need to remind myself to specify a system that has enough capability but *only* enough structure to let the system do its thing *via machine learning*. Give it a bit of inductive bias and then let it go to town on the data. Don't over-engineer.

It occurred to me in the context of thinking about [[Evolution LM - General Notes]] and how I should be using an encoder-decoder T5-like design for conditional embedding, and using semantic segmentation to chunk out data. And setting up a separate system to learn the evolution of the representation space. And by the way, that evolution should allow for a mixture of latents (and on and on, you get the idea).

But it seems like whenever I go down these rabbit holes, I come to the realization - either in hours or days or weeks - that, Hey, the conditional embedding idea is just *another way* to do attention! And a transformer with enough capacity and an LM loss function is probably doing semantic text segmentation and learning the evolution of representation space *anyway*. And maybe a modest structural change like adding MoE or beam search is the *better way* to allow it to learn a mixture of latents.

Sigh...