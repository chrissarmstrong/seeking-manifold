---
title: LLM Generation Degeneration
draft: false
tags:
  - post/thought
date: 2024-04-22
linkedin-promo: false
---
Over the last several months I've spent a fair amount of time [[Residual Stream Data Lane|training small language models]] on [small datasets](https://huggingface.co/datasets/roneneldan/TinyStories).

One of the things that I've noticed—and don't understand—is that when one of these models is fairly-well trained, but still slowly learning (coming down in loss or perplexity, choose your metric), the sample generation totally degrades from beginning of sample (a nicely told story) to end (unmeaningful, ungrammatical nonsense). See the example below.

I assume this is a completely obvious result of the autoregressive nature of the transformer being used, but somehow I'm not getting why it happens. At the end of the sample you are effectively dealing with a longer prompt, in which case I would naively expect the uncertainty over next tokens to go *down* (in the same way that perplexity is expected to be lower for a long piece of text). What am I missing?

## Example

### Beginning
>Once upon a time there was a prince who lived in a big castle. He was very happy and loved to play with his friends. One day, the prince went to the park with his friends. They played games and had lots of fun. But then, something unexpected happened. A big wind came and blew all the leaves away! The prince and his friends were very sad.

This is just what I expect. The LM is doing a good job modeling the TinyStories dataset it has been training on.

### Middle
>The moral of the story is to always be kind and help others and help others. We should always be kind and help others. We should always be kind and help others. We should always be kind to you and help others.

The LM is starting to lose it now. It has lost the plot of the story, and individual sentences are no longer coherent.

### End
>The end. The end. The moral value of you are the best friends. The end. You are better to you are better lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson lesson to you forgive forgive forgive forgive forgive forgive forgive forgive forgive forgive forgive forgive forgive forgive ...

At this point just about all semantics and coherence are totally out the window. (Note, however, that it still seems to recognize that it is at the *end* of the story instead of the beginning or middle!)
