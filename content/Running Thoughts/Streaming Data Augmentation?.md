---
title: Streaming Data Augmentation?
draft: false
tags:
  - "#post/thought"
date: 2023-01-02
---
With visual systems we typically make heavy use of data augmentation (cropping, resizing, rotation, color modification, etc.). This serves two purposes:
- It adds to the data we have;
- It acts as a regularizer, teaching the system to be invariant ("not care about") those particular transformations

Quick thought: Is this approach to data augmentation just a shitty way of working around the fact that we aren't using the *appropriate* sort of "augmentation", which is receiving a temporal stream of sensory input?

In other words, does our visual system get a similar training effect by virtue of getting a constant stream of input? And if so, does this latter approach result in more robust representations?