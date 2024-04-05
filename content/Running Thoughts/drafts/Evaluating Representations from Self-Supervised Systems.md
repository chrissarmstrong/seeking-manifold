---
title: Evaluating Representations from Self-Supervised Systems
draft: true
tags: 
date:
---
Some of the larger issues in AI that have come to the fore recently are around how we get systems to understand causality, to think and act hierarchically, and to reason. I've been paying attention to what Yann LeCun has been saying on these topics, and I think he makes a lot of sense.

In particular, I would like to get my head around how we might train JEPA systems[^1] to learn representations that allow for these capabilities.

One of the notable aspects of a JEPA is that it has no explicit generative component. Unlike a language model or a VAE or a GAN, it does not directly output something (text or image) that we can evaluate in a familiar domain.

So a question arises: how do we determine whether a JEPA system that we have trained in a self-supervised way has *learned meaningful representations*?  When training (say) a vision system, how does one judge the quality of the learned representations if we get no video predictions out?

From what I can tell, the work done to date has been mostly in the domain of images. In that scenario, the answer to the evaluation question is: *how well do the learned representations perform in downstream tasks?* For example, can we feed the representations into a classifier and (with few examples) train it to do successful image classification?

But if I'm interested in using video to solve for abilities like causality and reasoning, the answer is not nearly so clear (at least to me!).

Let's consider the problem very generally, and without the JEPA constraints: you have a black box system—think of it as an AI agent—into which you feed sensory information in order to have it learn about the world. You've designed a loss function to give it a learning signal. The loss goes down as the system trains, but what's to say that your loss function isn't garbage? What could you hope to get from that system to convince you that it had actually learned something meaningful?[^2]

This thought experiment turns on two aspects of the interface between the black box and the external world: 1) what is the nature of the information *into* the black box, and 2) what sort of information can flow *out of* the black box?[^3]

The inputs could be any number of things:
- static images
- video
- audio
- text
- other (haptic information, olfactory information, taste information, etc.)

Similarly, we could have a number of possible classes of output:
- raw representations (say the embeddings from an RNN or a transformer)
- text
- speech
- images or videos
- motion of some sort, if the agent is embodied (facial expression, body movements or actions, creation of various physical artifacts)

Here's something important to note: *all of those output types except the first assume that the system has some sort of generative ability*. The system may not be a generative system, per se—that is, it may not have a generative model at its core, of the type that LeCun wants to move away from—but it would certainly need some sort of generative ability to produce text, images, etc.

And it is surely the case that you or I, faced with an agent we had not interacted with, would expect to use generative outputs of a system to evaluate its intelligence (which I'm assuming are a floor for the quality of its internal representations). We could listen to it speak or look at the text or images that it generates and use that output to evaluate its representations.

Pulling back now from the general problem: if I'm trying to work on only a subset of the overall system, and output raw representations from video that captures causal interactions and the like, it's not so clear how to proceed.


(#working#)



(#part of me wants to say we need to 'bolt on' a generative capability.#)

At the moment I am concerned only about real-time sensory information in. For our purposes we can think vision and possibly audio.

The scenario with text in and text out, and a generative capability in our black box - what we have with LLMs - is fairly straightforward. While we can certainly argue all day about the details of how we're going to use the generated text out of a black box to judge the quality of the representations it has learned, we at least have a good starting point for the discussion. We're basically looking at a Turing Test-like situation, where we need some way to estimate the intelligence of the system.


If we get representations themselves out of the system (think embeddings of some sort), then one can argue that the usefulness of the learned representations (embeddings) will be reflected in their utility in various downstream tasks. This is what makes using features of BERT useful, and why linear probing is a thing.

(#and what if we have no generative capability? Talking about systems like LeCun's JEPA#)

If the system is capable of outputting text, then that offers one avenue for arriving at a judgement about what the system has learned. The text interface is exclusively how we evaluate current LLMs.[^4]



Hmm, matrix of input and output modalities?

this is how we judge humans and other animals that we interact with..

prediction... but issues with video prediction (as LeCun points out)

Some ideas in Fovea - General Notes in 2023-07-03 and 07-05 and 07-11. And 09-17. Causality is a big part of this.

Ideas:
- Measure some notion of 'surprise' (a la predictive coding), or energy, a la an EBM.
- How quickly can the system generalize to new tasks (Chollet)
- 


All of this has prompted my thinking about [[CIFAR for Video (Towards Simulated Environments for Self-Supervised Learning)|a CIFAR dataset for video]].


[^1]: (#LeCun Path towards Autonomous Intelligence ref#)
[^2]: 
[^2]: This is related to the problem of how you judge intelligence of a system - see, for example, François Chollet's [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) (2019). But this question of judging learned representations is really a precursor to that question of judging intelligence.
[^3]: There's also a question about whether information into the system is in any way conditional on the outputs of the system. In other words, is there a feedback loop between the output of the system and what it receives back? Here I'm assuming there is no feedback; but if there is, it begins looking like a reinforcement learning problem.
[^4]: The text interface is, of course, also at the heart of the Turing Test (with all its issues as a measure of intelligence).