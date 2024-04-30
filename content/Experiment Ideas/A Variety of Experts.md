---
title: A Variety of Experts
draft: false
tags:
  - post/idea
date: 2024-04-04
promo-linkedin:
---
I'm starting to play around a bit with a (very scaled down) mixture of experts (MoE) model. A few quick ideas that have come to mind:
- As Noam Shazeer points out in [one of the foundational MoE papers](https://arxiv.org/abs/1701.06538), you don't *have* to have all of the experts be identical. That begs the question: could you have different experts with different depths? Think of the router in a particular layer being able to pick a quick-and-easy expert vs a multiple-levels-of-complexity expert. Of course your forward pass will get slowed down any time your router chooses the latter.
- Could you benefit from having some sort of deterministic functions in some of the experts? Something that would help the network perform symbolic logic, for example?
- It would also be cool to go through the mech int exercise of having a dataset that had different types of data (say math vs history vs fiction) and seeing when the different types of experts get activated when dealing with each type of content.
