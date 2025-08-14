---
title: Predators in the Brush (A Taxonomy)
draft: false
tags:
  - post/thought
date: 2023-04-16
promo-linkedin: 2024-05-03
---
The heat is breaking now as the sun begins to set over the low mountains in the distance ahead of us. The five shadows of those in front have grown long, stretching back towards me over the golden grass of the savanna.

The breeze, which has been blowing most of the day, is now cooling. There is a constant hum of insects all around.

We know that we need to push on so that we make it to the foothills before it gets dark. This is not a place to be after the sun has set.

That is when it happens: a hush spreads out over the million insects until it is silent. Only the slightest rustling of the grass in the breeze. This has not happened to me before, but I've heard stories about it. *You never forget*, they said. *The silence happens first.*

At first I think maybe I'm imagining. But I see the others have stopped too. Maria turns back to look at me, her eyes growing wide. She has been walking with a long spear in one hand, and she raises it slowly.

And then we hear it: a rustle, faint but unmistakable, from the thicket to our left. Then a low rumbling noise. I think the earth beneath me shakes a bit. We are all frozen in place now, staring in the same direction, eyes scanning the brush for any sign of movement.

*Don't move yet*, I tell myself, heart pounding. I look down at my left hand. It is shaking. My right hand finds the knife tucked into my waistband. *Get ready, but **don't move yet**.*

---

This post was not written for you.

😛

It came about because I found myself struggling to understand the nature of the various risks that AI poses. 

I think it was in 2021 when I happened upon a piece by Eliezer Yudkowski. He immediately struck me as someone very smart, saying some really interesting things. I made a mental note to keep an eye out for his writing.

It wasn't long before I realized that all around me there was a rather vociferous debate going on about how AI will play out. The positions that people had staked out are all the way from *AI poses no danger whatsoever and will be the saviour of humanity* to *We are all going to be killed by AI and I've made my peace with that*. wtf? Notably, there were very intelligent people all across that spectrum.

The topic of AI risk also pulls me in multiple directions on a personal level. On one hand, I'm a [[Open Source Software|long-time advocate for open source]], and also believe that we should be pushing hard to democratize access to knowledge. And I'm a tech-inclined geek who enjoys research and tinkering with things. On the other hand, if some of the risks of AI are truly existential, I recognize the need for regulation and containment, even though that comes with its own very real set of problems.

This post began life for me, as a way to help me make sense of the AI alignment landscape; an attempt to articulate the taxonomy of these different risks posed by AI. Many people write more clearly and comprehensively about the risks associated with AI than I do, but often I find the need to work through things myself to better understand them. I expect my views to evolve as I consume more of the literature.

Specifically, my goal here was to take an initial step towards understanding alignment by first *categorizing the nature of the different risks*. Nothing more than that.

I find it helpful to keep this categorization in mind when talking to people or listening to debates. As is often the case with a topic new to society, it seems people are often talking past each other because their assumptions are not clearly stated.

---

Let's start with a diagram. Here's how I (currently) view the types of AI risk:

![[AI risks.png]]

There is admittedly overlap between the different buckets, and this is just one way of trying to organize things. That said, let's talk a bit about each of these.

## Bias & discrimination

This category is concerned with the issues that arise when we use AI systems in business and government to help us make decisions. A good resource for understanding the various types of bias that arise in AI / ML systems is [this paper](https://arxiv.org/abs/1901.10002) by Suresh and Guttag (2019).

This category includes things like bias in obtaining loans, getting jobs, and much more.

>[!info] Commentary
>These issues are real, non-trivial to address, and need to be cared for as we develop and deploy AI systems, but they are not my primary focus here.

## Economic and employment disruption

There are a whole set of issues that arise from AI augmenting or taking over different types of work being done today by humans, and the potentially huge ramifications that has for society.

>[!info] Commentary
>These issues are now widely discussed in the press. I'm of the opinion that AI will cause significant disruption, and that society needs to undergo some amount of restructuring to accommodate this.
>
>I fully expect that we will need to experiment with UBI-like policies to ensure that we have social stability as we transition to a world where the nature of work changes significantly. In my ideal world, traditional jobs become more or less optional; I may choose to have one, but other people may decide not to.

## Disinformation and algorithmic disruption

This is my bucket for impact from deliberate misinformation (think deep fakes) and the (intentional or unintended) effects of the use of ML algorithms in social media and other places we get information.

[This segment of The AI Dilemma](https://youtu.be/xoVJKj8lcNQ?si=Vhi-AjuCnEPqEO8X&t=419) is a bit dated but provides a good overview of the algorithm issue (and the rest of the video is well worth watching).

>[!info] Commentary
>I am of the belief—based largely on my own experience, not hard data—that social media and the algorithmic drive for monetization of engagement play a large role in the polarization we see in today's society and politics. Others (like Yann LeCun) disagree with this hypothesis. I would love to find some solid data on this one way or another.

## Population surveillance and manipulation

In this corner of the AI world we have risks associated with the use of systems to monitor and control populations of people.

>[!info] Commentary
>Any number of governments or other organizations around the world could do unspeakable damage if given advanced AI tools—even more so when combined with weapons, like in the next category.


## New weapons and easier access

There are real concerns about the ability of AI both to enable new and scary weapons and to democratize access to weapons. To start, think about automated drones, self-guided missiles, and the sort of thing we're beginning to see play out in the conflict in Ukraine. Further down the line you can imagine bioweapons, the ability to assassinate specific people from the other side of the planet, and more. Yikes.

>[!info] Commentary
>Setting aside for the moment the possibility of truly existential risks—which we leave for the next section—I view these issues as an exacerbation of problems we have even in the absence of AI.
>
>In other words, widespread availability of information—which I generally favor—enables this to some extent. AI may just put it on steroids.

## *Existential* risks

This set of categories is specific to scenarios that pose an *existential risk* to humanity or life in general on Earth.[^1] I split existential risks into three sub-categories: Unintentional, AI intentional, and Human intentional.

### Unintentional

The idea here is that an AI destroys humanity not due to malicious intent on the part of the AI or on the part of any human, but simply due to unfortunate circumstances.

>[!info] Commentary
>My shorthand[^2] for this is the 'anthill' scenario. Connor Leahy has likened the possible relationship between super-intelligent AI and humans to the relationship between humans and ants. Humans may, with no particular ill will towards ants, cause wholesale destruction of ant colonies simply because they happen to be in the way as we go about our business (of building a home, or laying a road, or building a dam, or whatever).[^3]

### AI intentional

This is a bucket for AI *intentionally* destroying humanity.

>[!info] Commentary
>My shorthand for this is the 'terminator' scenario. We all know this one from Sci Fi and the movies.[^4]

### Human intentional

This final bucket is for humans using AI in some way to intentionally end all human life (or all life, period) on Earth.

>[!info] Commentary
>My shorthand for this is the 'easy nukes' scenario.
>
>This is a reference to one of the scenarios in Nick Bostrom's excellent [Vulnerable World Hypothesis](https://nickbostrom.com/papers/vulnerable.pdf) paper (2019). The paper is very accessible and worth a read, but I'll summarize this particular vulnerability because I think people sometimes fail to account for its possibility when discussing AI.
>
>Consider the following thought experiment: it so happens that the laws of physics are such that building a large, life-ending nuclear weapon is *really quite easy*. All it takes are some simple ingredients available to anyone, together with some tools that are easy to acquire. Think sand + water + electricity together with a microwave oven, or something on that level.
>
>In that (alarming) thought experiment it seems fairly certain that soon after we discover the fact of easy nukes, humanity would be wiped out. There are enough mentally unstable, extreme misanthropes around that one or a few would decide to end it all for everyone.[^5]
>
>This scenario is important to consider because, if it ever comes to pass, it renders moot an assumption that many of us operate under in our normal lives, and even when considering AI risks: "Sure, there are a few bad people out there but vast majority are decent." That thinking doesn't mean squat if an 'easy nukes' situation exists.

## Other Factors

The above is my attempt at grouping the different types of AI risk. It doesn't address how or when those risks manifest. There are other considerations that play an important role in that part of the discussion. Let me touch briefly on a few of the biggest ones.

### Agency / AI drives / power-seeking behavior

Does an AI have agency? Can it have goals? Will it exhibit power-seeking behavior? If you think the answer is No, then several of the potential issues above just aren't very relevant, and addressing the dangers of AI is primarily about addressing the dangers of *people misusing AI*.

My take right now is that we need to be careful not to conflate consciousness (which we may or may not ever have in AI systems, assuming we can even properly define it) with some sort of drive or instrumental goals; the latter can be *engineered into a system*. It seems like we're already at the point where a sophisticated LLM could be designed into a larger agentic system that is programmed to pursue some goal at all costs.

### Molochian dynamics

If you are not familiar with the concept of Moloch, you really should be. As far as I'm aware, the modern framing is from [this fantastic post](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/) by Scott Alexander.

In brief: there are many situations in life where competition dynamics lead the actors to get stuck in a sort of race to the bottom in which everyone loses. Real-life examples abound, and once you are familiar with this concept you'll see it everywhere.

It has serious implications for the development and use of AI systems (as well as a number of other issues facing humanity).

I also highly recommend [this conversation between Liv Boeree and Daniel Schmachtenberger](https://youtu.be/KCSsKV5F4xc?si=ErUpLtELoXobTiWY&t=116).

### Evolution by natural selection

I've written a bit about this: [[Model Evolution by Natural Selection?]]

Basically, to the extent that AI systems evolve because we've set up the conditions for it to happen, then that introduces a dynamic that we won't fully control and may not even understand.

### Recursive self-improvement and superintelligence runaway?

The timing and speed with which AI systems advance, as well as who is in charge of that advancement, are important factors in how things will play out. If systems become capable enough to iterate on their own design, then the situation could quickly get out of human control.

## That's it for now

Hopefully this taxonomy proves a bit helpful. Feedback welcome.

\[Oh, sorry, I almost forgot... We got started with a little story. I don't know how it turns out yet. But just like our band of savanna travelers, we're on this journey together... 🙃 \]


[^1]: One could argue that whether a risk is existential should be a totally separate axis. But I think that the existential risks are distinct enough that we can 'flatten' the space and consider them separate categories. It helps to frame the issues.

[^2]: By 'shorthand' I mean an example that is emblematic of this category. At the risk of oversimplifying, the shortcuts do help me quickly remember where I am in the overall taxonomy.

[^3]: The ['paperclip maximizer' scenario](https://en.wikipedia.org/wiki/Instrumental_convergence#Paperclip_maximizer) was conceived by Nick Bostrom in 2003 to illustrate how a seemingly harmless system could—with sufficient intelligence and a lack of alignment—pose an existential risk to humanity as it attempted to accrue power and resources in furtherance of its goal to maximize production of paperclips. This scenario could fit in either the Unintentional or in the AI Intentional buckets, depending.

[^4]: How would one categorize a Matrix-like scenario, where the AI has relegated all of humanity to an existence in vats of jelly, to serve some purpose for the AI? Humans are still around, albeit not with a lifestyle many would consider worthwhile. I guess that one is open for debate.

[^5]: How many off-the-charts evil people are out there anyway? Let's take serial murderers as a rough proxy for extreme misanthropic behavior. A quick scan of [this page](https://en.wikipedia.org/wiki/List_of_serial_killers_by_country) and the referenced sub-lists shows that worldwide, there have been something like 2000 documented serial killers in the 20th and 21st centuries. Pretend for the moment that list captures all of the truly horrible, murderous people (which it certainly does not). If there have been maybe 15 B people alive in that period (being very loose with numbers here), that does mean the vast majority of people are not murderous by nature. But you get the point: if *every one of them* had the ability to end *all of humanity* because an 'easy nuke' button is available to all, then we are almost certainly doomed. Certainly one would pull the trigger.
