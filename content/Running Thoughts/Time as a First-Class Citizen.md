---
title: Time as a First-Class Citizen
draft: false
tags:
  - post/thought
date: 2023-03-18
linkedin-promo: false
---
One of the things that has bothered me the most since starting to learn about AI / ML systems is that they often treat the passage of time as a second-class citizen, if at all.

Time—in particular the continuous *flow* of time—plays an absolutely central role in the lives of humans and other animals. I won't talk about consciousness—I'm not very good at wrestling such slippery topics into submission—except to point out that I could not even *imagine* it devoid of the flow of time.[^1]

Even sticking to more tractable topics, the list of ways in which time factors into animal lives is long:
- Learning is continuous and 'on line'
- Attractor states play important roles in the operation of human and other animal brains
- Feedback loops and recurrence are everywhere in the brain
- There are numerous short-timescale processes like temporal coding, spike timing, neural oscillations, phase locking mechanisms, temporal integration of stimuli and motor control, eye saccades, spontaneous activity patterns in the visual system, etc.
- We have the daily circadian rhythm and the sleep-wake cycle
- We have a continuous predictive coding process happening in which we have expectations / anticipations that are either met or not (and when the latter happens it kicks off other downstream processes)
- Our brains make heavy use of experience replay
- Our vision system has the dorsal visual stream, which deals specifically with motion
- We have several memory processes, from short-term to long-term; our memory systems suffer from temporal encoding clashes (learning two things at about the same time inhibits retention / retrieval)
- Our brains never stop developing, from the time we are in the womb until we die.[^2] There is some evidence that our genetics encode simple rules defining dynamic systems that then generate structure in the brain.[^3]

But it feels terribly reductionist to even *list* those things; in reality they are all intertwined effects in a dance through time (at least for the short period that we're alive).

This is mostly missing from current AI systems.

Yes, there are exceptions:
- Robotics are arguably the closest systems we have that—of necessity—deal with time
- Time plays a definite role in spiking neural net (SNN) systems
- Some video classification systems use the concepts of [temporal attention](https://arxiv.org/abs/2102.05095) or ['flow'](https://arxiv.org/abs/1406.2199)
- Some ML systems by their very nature deal with time-domain signals (e.g., audio)
- Work by Geoffrey Hinton and a few others has touched on sleep-wake cycles
- Some RL systems use a rather crude analog of experience replay
- There have been some notable efforts towards curriculum-based learning (primarily in vision systems and LLMs)

But these feel like they are either tangential invocations of time-based processes or modest attempts to deal with a small piece of the puzzle at a time. They are not time-based *through and through*, at their core.[^4]

Something in my gut tells me that having time play a central role in our AI systems is going to be critical for getting them to understand causality, object permanence, interactions with 3D systems, and physics; be able to perform complex, hierarchical long-term planning; be robust to adversarial attacks, and so on. I would love to help figure out how we make that happen.

[^1]: I quite like Karl Friston's discussion on consciousness [in this article](https://aeon.co/essays/consciousness-is-not-a-thing-but-a-process-of-inference).

[^2]: Check out [The Development of Embodied Cognition: Six Lessons from Babies](https://www.semanticscholar.org/paper/The-Development-of-Embodied-Cognition%3A-Six-Lessons-Smith-Gasser/25f8e9e35cafd7fb686d939f274111bcffeafd6b) by Smith and Gasser (2005).

[^3]: See [Why the Brain is So Noisy](https://nautil.us/why-the-brain-is-so-noisy-237301/) for an interesting and accessible read.

[^4]: I have to confess that I'm really failing to convey what I'm thinking about here, almost to the point that I need to regroup and start again. Apologies.
