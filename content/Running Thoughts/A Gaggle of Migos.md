---
title: A Gaggle of Migos
draft: false
tags:
  - post/thought
date: 2024-04-23
linkedin-promo: false
---
A while back I posted some musings about the ramifications of [[Migos|the Migos we will all soon have in our lives]].

It occurred to me after writing that piece that if you aren't one of the folks who tend to hang around places like [the LocalLLaMa sub-Reddit](https://www.reddit.com/r/LocalLLaMA/), where people use large language models (LLMs) for RP (role-play), then you may be out of the loop on what modern open LLMs are capable of.[^1]

Many people presumably are exposed to LLMs by using ChatGPT (the OG of truly modern LLMs) or one of the many similar ones trained and hosted by other companies. There are a lot of really good ones out there, if you're looking for *answers to questions* instead of, say, a list of search hits. I personally like You.com, Phind, and Perplexity, and I use them every day. There are also ones from Google, Microsoft, and others.

But those LLMs are designed specifically to be assistants that help you out without ever offending or doing anything untoward. Their corporate owners (understandably) do not want to be responsible for a modern-day [Tay](https://en.wikipedia.org/wiki/Tay_(chatbot)). As a result, these bots are the epitome of anodyne. And if this type of bot is all you've seen, *you really need to get out and meet more bots* 😛

What I want to do here is take you through a quick and hopefully interesting exploration of what a modern, relatively small LLM is capable of.

We're going to play with a single model (the recently-released Llama-3-8B from Meta; thanks to Zuckerberg and team!). I'm going to set up a handful of different 'characters' and then ask each character the *exact same question*. The point of this exercise is very simple: *pay attention to the variety of responses that we get to that same question*.

How am I creating different characters? All I'm doing is prefacing the interaction with a bit of text (a paragraph or two) that contains a description of the character and maybe some example interactions. I've summarized this character description before each of the interactions below.

A few additional notes:
- Unlike the models mentioned above, the model we're using here is not connected to the internet or any external sources of information; everything it 'knows' is baked into its weights during training.
- The model is fairly small—8 billion parameters, compared to the models above which range anywhere from 30 billion to perhaps 1 trillion parameters. It runs on my desktop machine with my modest GPU.[^2]
- I've chosen the names of the characters to reflect their background or personality; this seems to help them stay in character.
- I've equipped the different characters with avatars that were—you guessed it—created by another AI based on the character descriptions.
- I'm showing screenshots of the conversations because I think it helps convey the conversational tone better than a wall of text.

Here we go, starting with Amanda Bot. Our question—again, the same for each character—has to do with legal issues around immunity for US presidents, which some of our characters will be better positioned to address than others. Also remember: everything here is using *the exact same LLM*, the only difference is the couple of paragraphs of text describing the character that I've prefaced each interaction with.

#### Amanda Bot is my Amanda Marcotte (salon.com) stand in, with a razor-sharp wit and a passion for progressive ideology. She doesn't hold back.

![[immunity-amanda.png]]

Very interesting that Amanda Bot called out Trump without me leading her in that direction. But this model was trained on data up until 2023, so it does know about recent events!

#### Tyke is a 5 year old. Good kid, and bright. But only 5!

![[immunity-tyke.png]]

That kind of gets right to the point, doesn't it?

#### Justice Jedi is a young, highly-regarded (and fiery!) legal scholar and US Constitutional expert.

![[immunity-justice.png]]

Justice seems to know her stuff, although I believe the reference to Butterfield v. United States is a hallucination. The other cases she cites do exist, although I can't speak to her characterization of them.

#### Heritage Hank is extremely conservative (politically, socially) with a tendency towards authoritarianism.

![[immunity-heritage.png]]

Hank sure stepped out of character there on Clinton!

#### Señorita is a student at Columbia University. She has a quirk: she understands English perfectly well, but she *only responds in Spanish*.

![[immunity-senorita.png]]

Pretty impressive, for a model that was not explicitly trained on translation!

#### Cigs N Booze is a hopeless degenerate, but a funny guy for someone who is so dark and broken. Somewhere underneath his grungy, noxious exterior you can see a glimmer of humanity, though he does his best to keep it hidden. And be forewarned, the dude has a nasty mouth.

![[immunity-cigs.png]]

Cigs has had a tough life. Don't judge until you've walked a mile in his shoes.

#### Polly Mind is a brilliant scientist and polymath. She is well-versed in physics, genetics, mathematics, chemistry, and biology.

![[immunity-polly.png]]

I'm not buying the connection to physics, but not too bad.

#### History Wise is a historian and author of a number of books ranging from religion to language to psychology.

![[immunity-history.png]]

Ms. Wise def knows the subject matter as well.
#### And last but not least, Flux the Cat. Flux is a character I didn't define, I came across him somewhere. The important thing to understand is that—well—Flux is a cat!

![[immunity-flux.png]]

*hiss??*

Yikes! Then again, I'm represented by a mouse. I should be thankful it didn't get any worse than that 😅

At any rate, I hope that gave you a sense of the diversity that exists within a single LLM, and what interacting with one can be like. The thing has been trained on *many* more books and articles than you or I will ever read, and so it has been exposed to all kinds of stuff. It contains in its weights the information needed to mimic all kinds of personalities. You just have to tease it out.

I also think about it like this: This may well be the *least* capable, *least* knowledgeable language model I'll interact with in the future. In a few years I will look back on this post like I now look back on [[CLIP Guided Diffusion|my old post about early text-to-image systems]]: "Aww, how quaint!"


[^1]: I'm not into role play, per se, but I do use the tools to do the sort of model exploration I show in this post.

[^2]: I'm running the instruct version of the model quantized to 6 bits per weight, using text-generation-webui and/or ollama, front-ended with SillyTavern. For those who may care.
