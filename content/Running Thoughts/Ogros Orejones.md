---
title: Ogros Orejones
draft: false
tags:
  - post/thought
date: 2025-12-04
promo-linkedin:
---
I stick to my belief that the current LLM technology is unlikely to (by itself) get us to human-level machine intelligence. I also believe that in many ways the current tech is over-hyped, and we're due for a bubble to pop. Certainly [the amount of money flying around is insane](https://www.youtube.com/watch?v=pQ0zrQaYt3k).

That said, I sometimes step back and can't help but marvel at where we are. And sometimes it is the seemingly simple things that hit home.

Here's an example: in an attempt to (again) learn Spanish, I'm reading through a few kid's books. Sometimes the content that a first-grade Spanish speaker would understand is a bit beyond me.

![[minicpm-y-ogros-orejones-1 1.png]]

I know some of the words, but not all, and I just don't get what is going on (or why it would be entertaining for a kid).

Nowadays, we can have local models that are quite capable. I pass in the image to one of these (in this case, MiniCPM-V 4.5[^1]), and ask it:

> This image is from a Spanish children’s book. Can you translate the text and explain it to me?

Here's what I get back a moment later:

![[minicpm-y-ogros-orejones-2.png]]

Is this perfect? No. Is this a particularly sophisticated example? Far from it. Still, it is pretty remarkable. If you had told me back in ~2020 (before GPT-based models surprised just about everyone with their ability to generate coherent text) that we'd be here today I would have been very skeptical.

Ignoring technical details about how this particular vision-language model works, it has:
- Performed optical character recognition (OCR) on an image that has chunks of text scattered around the page, interspersed with images. This itself is pretty impressive, at least to someone who has experienced the brittleness of previous-generation OCR.
- Translated Spanish to English pretty well.
- Been able to describe what the different images on the page are (and the fact that they are separate images)
- Been able to integrate the translated text and the descriptions of the images into a cohesive explanation of what is going on, associating the different pieces of text with the corresponding image, etc.

This feels like we're steadily chipping away at [Moravec's paradox](https://en.wikipedia.org/wiki/Moravec%27s_paradox) (specifically the perceptual component, as opposed to the motor component). The ability to look at a page and quickly understand the gist of what is happening is something that until recently seemed easy for a human but out of reach for a machine.

[^1]: Note that this is a small-ish model, and not connected to the internet. Everything it 'knows' is contained in the 8 billion parameters in the model. And it runs just fine on a modest, old-by-many-standards (2018 era) machine.