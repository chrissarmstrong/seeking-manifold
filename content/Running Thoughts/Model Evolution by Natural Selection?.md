---
title: Model Evolution by Natural Selection?
draft: false
tags: 
date: 2024-04-16
---
Two trends I find fascinating are fine-tuning of models and performing model merges. Most of you are probably familiar with these concepts, but a few words in case you aren't.

## Fine Tuning

The creation of a base or instruction-tuned large language model (or LLM) is largely beyond the reach of individuals or even many organizations; because of the resources (hardware, expertise, energy) needed, it can cost millions of dollars or more.[^1] But once you have a pretrained model, fine-tuning it—basically tweaking it to perform better on a specific set of tasks, typically using a small-ish dataset—is a much more modest task. For smaller LLMs (oxymoron?) it is within reach of just about anyone. If you don't have a suitable computer, for a few dollars you can rent a cloud-based machine on which to do it.

## Model Merging

Model merging is pretty much what the name implies. There are now a number of ways to take two or more models (typically fine-tuned from the same base model) and smoosh them together. There's a lot of excitement around merging because we've found that merges often combine the best capabilities of their constituents.

For example, I can take two variants of a model—one fine-tuned to do better on math, and the other fine-tuned to do better on coding—and merge them to get a model that does well on both math and coding tasks. So cool!

Model merging is just as accessible as fine-tuning; it is now quite doable for someone with a computer and a bit of know-how. I went to Hugging Face today and I see that there are 79k text generation models; a good number of these are merged models.

In the current ecosystem, people find the model variants that do best on some benchmark, or just the ones that they prefer to interact with, and merge them to see what they get.

## Evolution by Natural Selection

All of this brings me to the point of today's post: a paper I read a while back, [Natural Selection Favors AIs over Humans](https://arxiv.org/abs/2303.16200) (2023). In this paper Dan Hendrycks lays out his arguments that AIs will be subject to evolution by natural selection by virtue of humans modifying and propagating the ones they find most useful, entertaining, etc. Sound familiar?

Hendrycks reminds us of the Lewontin conditions, which many of us learned about in high school or university biology class. These are the conditions that need to be in place for evolution by natural selection to take place. In brief:

1. **Variation**: There must be variation in the phenotypes of a population. In other words, there must be differences in the traits of individuals within a population.
2. **Heritability**: The variation that is expressed must be heritable. That is, these traits must be passed on from one generation to the next.
3. **Fitness**: There must be a difference in fitness between the phenotypes, such that something in the environment preferentially selects some traits over others, hence some traits end up more likely to be passed on to the next generation.

At face value it seems clear that this idea—of creating variants of models, merging them together, and selecting the ones we like the most—results in an environment for AI models that meets the Lewontin conditions. The model fine-tuning supplies the variability, then the merging passes traits on from one generation to the next, and human preferences about which models get fine-tuned and merged ensure that some traits are passed on while others fall by the wayside.

Have we have created the conditions necessary for our AIs to evolve by natural selection?!

While this is a really interesting and even exciting thought, it is also somewhat troubling. Invoking evolution in systems that are becoming quite capable in many tasks and that we really don't understand is a bit scary.

Evolution can result in some scary shit. If you don't think that's the case, it may be that our collective civilizational respite from the harsher realities of survival among evolved organisms has allowed you to forget that [nature is metal](https://www.reddit.com/r/natureismetal/).

Hendrycks' paper is very thought-provoking and worth a read.

### Postscript

Looking for weaknesses in this line of thinking, I posed the following query to several of the best LLMs:

>The Lewontin conditions specify the conditions under which evolution by natural selection occurs.
>
>The recent trends of fine-tuning and merging large language models, and then selecting which of those we want to continue working with, would seem to meet the Lewontin conditions, and indicate that we now have the conditions for evolution by natural selection in AI systems.
>
>Give me well-reasoned arguments *against* this line of thinking. They could be arguments that for some reason we are not creating the conditions for evolution by natural selection in AIs, or arguments that the Lewontin conditions do not apply to this situation, or arguments that the Lewontin conditions are somehow not correct, or arguments that evolution by natural selection somehow does not apply to AI systems, or other arguments altogether.

I won't post the LLM responses here (I encourage you to try it), but I did get some interesting ones. They were articulate and thoughtful, albeit not completely convincing.

But most interesting of all is the fact that my inclination was to ask AIs about this situation in the first place!

[^1]: Although the resources needed for pretraining are decreasing pretty quickly. It may be that in a few years it is within reach to pretrain your own rather large model from scratch.
