---
title: Evaluating Representations from Self-Supervised Systems
draft: false
tags:
  - post/thought
date: 2024-04-12
promo-linkedin:
---
Some of the larger issues in AI that have come to the fore recently have to do with getting systems to understand causality, to think and act hierarchically, and to reason. I've been paying attention to what Yann LeCun has been saying on these topics, and I think he makes a lot of sense.

In particular, I've been thinking about how we might train [Joint Embedding Predictive Architecture, or JEPA, systems](https://openreview.net/forum?id=BZ5a1r-kVsf) to learn representations that allow for these capabilities.

One of the notable aspects of a JEPA is that it has no explicitly generative component. Unlike a generative language model or a VAE or a GAN, it does not directly output something (say text or image) that we can evaluate in a familiar domain.

So a question naturally arises: how do we determine whether a JEPA that we have trained in a self-supervised way has learned *meaningful representations*?  Namely, when training a vision system how does one judge the quality of the learned representations if we get no image or video predictions out?[^1]

From what I can tell, the JEPA work done to date has been in the domain of images and (more recently) video. In these scenarios, one possible answer to the evaluation question is: *How well do the learned representations perform in downstream tasks?* For example, we might feed the learned representations into a decoder + classifier and (with few samples) attempt to train it to do successful image classification. Or feed videos into a decoder + classifier and attempt to train it to do successful action classification.

But if we're interested in using video to solve for abilities like understanding *causality* and performing *reasoning*, it's not clear to me that the answer is as simple as that.

## A general framing

Let's consider the problem more generally, and without the JEPA constraints: you have a black box system into which you feed sensory information in order to have it learn about the world. You've designed some sort of loss function to give it a learning signal. The loss goes down as the system trains, but what's to say that your loss function isn't garbage? What could you hope to get from that system to convince you that it had actually learned something meaningful?

This thought experiment turns on (at least) two aspects of the interface between the black box and the external world: 1) what is the nature of the information *into* the black box, and 2) what sort of information can flow *out of* the black box?

![[content/images/black-box-training.png]]

The inputs could be any number of things:
- images or videos
- audio
- text
- other things like haptic information, olfactory information, taste information, etc.

Similarly, we could have a number of possible classes of output:
- raw representations (like the embeddings from an RNN or a transformer)
- text
- speech
- images or videos
- actions or motion of some sort, if the agent is embodied (facial expression, body movements or actions, creation of various physical artifacts)

Here's something important to note: *all of those output types except the first one assume that the system has some sort of generative capability*. In those scenarios, while the system may not have a generative model at its *core* (the type of system that LeCun wants to move away from), it would at least need a generative capability 'bolted on' to produce text, speech, images, etc.

And it is surely the case that you or I, faced with an agent we had not previously interacted with, would expect to evaluate its intelligence using its generative outputs. In other words, we could listen to it speak or look at the text or images that it produces to get a sense for the quality of its internal representations.[^2]

## How do we test our system's representations?

Stepping back now from the general problem posed above: I would like to develop a JEPA system that learns internal representations capable of supporting causal understanding and reasoning. My gut tells me that we should start with visual observations (in particular, video). While intelligence can obviously develop in the absence of visual input, much of what we think about as causality and reasoning is, at the very least, highly informed by what we learn from the visual domain.[^3]

Next, assume that we've trained some system on visual input. Now we're faced with the problem of evaluating those internal representations. How to proceed?

I don't have great answers here, but I wanted to capture my thinking. Here are some notes on potential approaches.

### 1. Test raw internal representations

As noted above: could we use internal representations for some task that proves they've incorporated suitable knowledge from their experience? The trick here, I believe, is coming up with meaningful tasks that could test for understanding or awareness of the things I really care about, like:
- basic physics
- object permanence
- causal reasoning
- counterfactuals
- interventions
- anomaly identification
- directly interpretable representations (a la OthelloGPT)

Specifically, I'm skeptical that testing representations on tasks like image or action classification ("this is a dog" or "the person is picking up an apple") is sufficient to ensure that they capture information about causality, etc. I think we would need to expand the type of tasks to better account for these qualities.

### 2. Add a generative capability

To me, the most obvious and intuitive solution to this problem is to add a generative capability to the system. This allows it to communicate with us in a way we can understand.

For example, if a system can show you text that makes sense, or utter something you understand, or create an image that you recognize, then that tells you a lot about what it has learned. This is how we draw conclusions about a new person we meet, or a new animal we encounter. It is also how we typically judge modern LLMs; when they have low perplexity, they can do a reasonable job of continuing text (or if instruction-tuned, actually take part in a conversation).

This approach assumes that we have some way of translating from a representation space to whatever domain we want for our communication.

### 3. A probing signal

The idea here is somewhat analogous to how we know that infants or other animals (who don't share our spoken language) are making sense of their environment. My favorite example is the expression of surprise; when you show an infant something unexpected (like a magic trick), they show clear astonishment or surprise, which tells us that something doesn't match their world model. This effect is used in experiments (with infants) as a sign that the subject has observed something unexpected.

Could we similarly probe a neural network to monitor something like surprise? Then we use the presence of that signal to indicate that the network has seen something that doesn't make sense to it. For example, we might feed a series of videos to the system, looking at this signal, and periodically add in a video that includes a physically-impossible scenario.

I should note that this type of signal feels a *lot* like the energy in an energy-based model (EBM). In fact, I rather expect that someone well-versed in EBMs would tell me that is effectively what I'm talking about here.

One of the challenges here would be differentiating between a signal for surprise due to (say) non-causality ("this situation cannot be!") versus one for general novelty ("I've never seen a situation exactly like this one, but it seems plausible").

## Next?

This post falls into the category of "trying to sort things out in my mind", as opposed to proposing answers. I find myself struggling to figure out the best way forward here.

I'd love to hear what you think!


[^1]: This is related to the problem of how you judge intelligence of a system - see, for example, François Chollet's [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) (2019). IMO this question of judging learned representations is really a *precursor* to that question of judging intelligence.

[^2]: Here I'm assuming that quality internal representations are a prerequisite for intelligence. Seems reasonable to me, although I present it without proof.

[^3]: All of this has informed my thinking about [[CIFAR for Video|a CIFAR dataset for video]].
