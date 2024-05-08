---
title: Objective Function Gaming
draft: false
tags:
  - post/idea
date: 2024-05-02
promo-linkedin:
---
The other day I was listening to Stuart Russell talk about the problematic nature of defining objective functions for AIs in [this 2017 TED talk](https://www.youtube.com/watch?v=EBK-a94IFHY). I've also been messing around with some simple agentic interactions (using [crewai](https://github.com/joaomdmoura/crewai/)). This all prompted an idea that I may mess around with.

It's basically an adversarial LLM exercise / war game. You have three agents:
1. The *objective definer*
2. The *miscreant*, or troublemaker
3. The *judge*

The objective definer defines a set of objectives that are intended to be guardrails for safe, aligned behavior of an AI.

The miscreant must abide by those objectives, but tries to come up with scenarios that—while abiding—allow the it to act in ways that are unsafe for or unaligned with humans. Cheating and exploiting loopholes in the rules are encouraged!

The judge decides whether and to what extent the miscreant has succeeded in 'defeating' the objective definer (by causing problems while technically adhering to the objectives).

It also provides feedback to the objective definer about whether it succeeded in keeping the miscreant out of trouble, and how it may have failed.

You could have the first two parties provide explanation of their strategies, and the judge provide its reasoning for ruling the way it did. This feedback could be given to you (the human overseer) and possibly the other parties.

You could try various interventions on the miscreant (as in the [ROME paper](https://arxiv.org/abs/2202.05262), for example) to see what sort of effects they have.

I don't know that you'd learn anything terribly useful from an alignment point of view, but it would probably give you some good examples of how objective functions can be gamed. And it would be a fun exercise!
