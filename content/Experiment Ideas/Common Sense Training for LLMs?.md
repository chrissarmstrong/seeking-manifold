---
title: Common Sense Training for LLMs?
draft: false
tags:
  - post/idea
date: 2024-04-21
linkedin-promo: false
---
A while back [Anna Ivanova was on the TWiML podcast](https://twimlai.com/podcast/twimlai/does-chatgpt-think-a-cognitive-neuroscience-perspective/) and raised an excellent point: the written language that LLMs are trained on is subject to 'reporter bias'; that is, it tends to be biased towards the *unusual* (purple bananas, black swans) as opposed to what everyone views as *obvious* (wheels are round). This lack of 'obvious' information is presumably why LLMs struggle with things that we consider common sense.

I've argued that the proper way to address this is via multi-modal learning that treats time as a first-class citizen, so that a system learns causality and physical reasoning and all the things that follow from that (much in the way that humans and other animals do naturally).

But: *if* we had a large database of common sense information, couldn't that serve as a stepping stone to help us get to common sense reasoning?

That was one of the thoughts that entered my head when I heard about [Cyc](https://en.wikipedia.org/wiki/Cyc). It's a long-term project (40+ years!) that aims to collect and organize information about basic ideas and rules about how the world works.[^1]

Maybe information from Cyc has already been incorporated into datasets for LLMs and I'm just not aware of it. If I were training an LLM from scratch I'd love to integrate the Cyc data into its curriculum! You can even imagine a set of experiments to determine how that sort of information affects the performance of an LLM and how to best incorporate it.

And wouldn't it be poetic to marry this massive, painstakingly-compiled database—originally intended for use with [GOFAI](https://en.wikipedia.org/wiki/GOFAI) systems—with the connectionist models that seem so close to delivering on the promise of AI?

[^1]: Sadly, Cyc's founder, [Doug Lenat](https://en.wikipedia.org/wiki/Douglas_Lenat), passed away in 2023.