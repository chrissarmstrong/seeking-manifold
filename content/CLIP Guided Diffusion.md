---
title: CLIP Guided Diffusion
draft: false
tags: 
date: 2021-12-18
---
## Update 2024-03-04

I put this page together in late 2021 when text-to-image generation was in its infancy and I was blown away by what was happening. Now it feels really outdated, almost quaint, and I leave it here as a kind of signpost of how quickly this field has advanced, and a reminder of why I became motivated to dive into AI / ML.

## A Quick Intro

Like many (many!) others, I've been playing around recently with systems that can create 'AI art', mostly with one called "CLIP Guided Diffusion". I didn't come up with this idea or write this code myself; credit for that goes largely to [Katherine Crowson](https://twitter.com/RiversHaveWings) and the Colab notebooks she has been releasing to the world. I'm running code derived from those (but doing so locally).

What is CLIP Guided Diffusion, you ask? In a sentence, it is a system that takes a piece of text and creates images that it thinks are a good representation of that text.

![[clip-guided-diffusion.png|CLIP Guided Diffusion]]

How does this work? Here's a brief explainer: There are two models at the heart of the system. The first one, CLIP, is [a model](https://github.com/openai/CLIP) released by [OpenAI](https://openai.com/). The special thing about CLIP is that it was trained on a lot of image / caption pairs in such a way that it encodes both images and text into a common vector space, attempting to keep the representations of the pairs close by in that space. So for example if I create embeddings of the words 'dog', 'canine', and a picture of a dog, these will all be fairly close in this vector space, while the text 'house' and a picture of a house would be off in another area of the vector space.

Now if we couple CLIP with a second model that can generate images and that we can backpropagate through, we can give that text to CLIP and it can iteratively 'guide' the generative model towards images that are near the embedded text prompt in our representational space.

For those interested, [LJ Miranda](https://ljvmiranda921.github.io/) has some nice historical notes on the players who created this concept, relevant references, and a more in-depth explanation of how the earlier VQGAN-CLIP code works [in this post](https://ljvmiranda921.github.io/notebook/2021/08/08/clip-vqgan/). (2022-01-03 edit: [This post](https://ml.berkeley.edu/blog/posts/clip-art/), by Charlie Snell, gives a really good historical overview of the various approaches and how they came together in 2021, but it predates the guided diffusion approach.) CLIP Guided Diffusion is conceptually the same as VQGAN-CLIP but uses a different type of model to do the image generation: [Guided Diffusion](https://github.com/openai/guided-diffusion) (also released by OpenAI). From what I've seen, the guided diffusion approach to generating images seems to be more expressive and visually coherent than VQGAN.

The code I've been running lately is based on [this Colab](https://colab.research.google.com/drive/1FuOobQOmDJuG7rGsMWfQa883A9r4HxEO?usp=sharing), which has done a great job speeding up Ms. Crowson's [CLIP Guided Diffusion notebook](https://colab.research.google.com/drive/12a_Wrfi2_gwwAuN3VvMTwVMz9TfqctNj). I generate about one 256x256 image per minute on my middle-of-the-road GTX 1070 GPU (I can't generate 512x512 with my limited GPU memory).

My routine is to get my machine working on maybe 50 or 100 images from one text prompt (overnight or when I'm stepping away for a bit). I then select the ones I like best (which is typically about 5 - 10% of them) and run those through (the very impressive) [Real-ESRGAN super resolution model](https://github.com/xinntao/Real-ESRGAN) to increase the size to 1024x1024.

What follows is a quick tour through some of my favorite images after having played with this for a few weeks. My focus here is on the art created by the AI more so than the prompt engineering that is behind the creations. Rather than identifying the specific prompts used to create each image, I'm using CLIP by itself to do searches through my collection of ~500 favorites. As we go I'll provide a bit of commentary about prompt engineering and the interesting ways in which CLIP sometimes behaves.

## Victorian Era Portrait of a Woman

Let's start with this search: "Victorian Era Portrait of a Woman". So again, I'm asking CLIP to find (in my collection of 500 favorites) the images it thinks most accurately match that phrase.

![[array-victorian.png|Victorian Era Portrait of a Woman]]

And in this case, the first 5 images CLIP selected were in fact created using that prompt or one very similar (e.g., "Victorian era portrait"). The last image, it turns out, was created with the prompt "Window into a beautiful soul #artstation", but you can see how it's not _too_ bad a match for a Victorian era portrait!

## Beautiful Orchid

Here CLIP is finding the images in my favorites that it thinks most closely match "beautiful orchid".

![[array-beautiful-orchid2.png|Beautiful Orchid]]

And in fact all of these images were produced with that prompt or a similar one (e.g., "beautiful orchid #artstation" or "watercolor of an orchid").

## Beautiful Colorful Fish

![[array-beautiful-colorful-fish.png|Beautiful Colorful Fish]]

They are beautiful. And colorful! And all created with the prompt "beautiful colorful fish (trending on artstation)".

## Beautiful Pattern

![[array-beautiful-pattern.png|Beautiful Pattern]]

## Eye of Sauron

![[array-eye-of-sauron.png|Eye of Sauron]]

## Child's Drawing

![[array-childs-drawing.png|Child's Drawing]]

Images 1, 2, 3, and 6 were from the prompt "Mommy and Daddy, drawn by a child". Image 4 was "watercolor painting of an owl". Image 5 was "alien scribblings on a blackboard". But they're all a decent match for the search term "child's drawing".

## Hotel California

![[array-hotel-california.png|Hotel California]]

Image 5 was from the prompt "a beautiful winter scene in an old town with Christmas lights (acrylic painting)". The rest were all "Hotel California. You can check out any time you'd like, but you can never leave (trending on artstation)".

You've probably noticed that some of the prompts used to create the images contain stylistic elements, like 'trending on artstation' (see [Trending on Artstation](https://www.artstation.com/?sort_by=trending)) or 'watercolor' or 'acrylic painting'. It turns out that CLIP, in the course of its training, saw enough images with captions containing stylistic information that it now has an opinion about what a watercolor painting is, and can steer the generative model in that direction!

## Owl

![[array-owl.png|Owl]]

Prompts here were all variants on "owl": "an owl made of voxels", "xray owl", or "watercolor painting of an owl". Can you tell which are which?

## Leaves in Fall

![[array-leaves-in-fall.png|Leaves in Fall]]

## Shenandoah Mountains

![[array-shenandoah-mountains.png|Shenandoah Mountains]]

The last image here was actually from an "owl"-based prompt, but it's not a bad fit!

## Old Father Time

![[array-old-father-time.png|Old Father Time]]

It's cool how some of the Old Father Times incorporate the notion of a clock.

## Sand in the Hourglass

![[array-sand-in-the-hourglass.png|Sand in the Hourglass]]

The first five here were generated with the prompt "sand in the hourglass #artstation"; the last was "leonardo da vinci invention sketch".

## Old European Town at Christmas time (oil on canvas)

![[array-old-eu-town-at-christmas-oil.png|Old European Town at Christmas time (oil on canvas)]]

## Paradise on Earth

![[array-paradise-on-earth.png|Paradise on Earth]]

## Martian Sunrise

![[array-martian-sunrise.png|Martian Sunrise]]

# Now for a detour into some darker places...

In this 'darker' section, the prompts and the search strings tended to be more abstract. As a result, there's a lot more 'crossover' from one prompt to a different search string. And you'll notice that some images show up in more than one search.

## Dark Night of the Soul

![[array-dark-night-of-the-soul.png|Dark Night of the Soul]]

## Evil Queen

![[array-evil-queen2.png|Evil Queen]]

## The Grim Reaper

![[array-grim-reaper2.png|The Grim Reaper]]

## Mysterious Dark Queen of the Afterlife

![[array-mysterious-dark-queen-of-the-afterlife2.png|Mysterious Dark Queen of the Afterlife]]

## Monster

![[array-monster.png|Monster]]

## Feeding the Beast

![[array-feeding-the-beast.png|Feeding the Beast]]

Several of the prompts here included "by Greg Rutkowski". Greg is a prolific artist whose work you can see on Artstation, and he has a very distinct style. Here too, it seems that CLIP has a pretty good understanding of Rutkowski's style.

## Conquering the Fear Within

![[array-conquering-the-fear-within.png|Conquering the Fear Within]]

Note that we sometimes get attempts at artist signatures on paintings.

## Abomination

![[array-abomination.png|Abomination]]

## The Gates of Hell

![[array-gates-of-hell.png|The Gates of Hell]]

## The Hounds of Hell

![[array-hounds-of-hell.png|The Hounds of Hell]]

# Let's get back to some lighter fare

## Flower in the Shape of a Heart

![[array-flower-in-the-shape-of-a-heart.png|Flower in the Shape of a Heart]]

## Window into a Beautiful Soul

![[array-window-into-a-beautiful-soul.png|Window into a Beautiful Soul]]

I like the doggo through the window. Good boy!

Funny here that image 5 is supposed to be an eye of Sauron, and the prompt for image 6 was "conquering the dark fear within #artstation". Beautiful soul indeed.

## Hearts and Flowers

![[array-hearts-and-flowers.png|Hearts and Flowers]]

## Love and Marriage

![[array-love-and-marriage.png|Love and Marriage]]

## The Tree of Life

![[array-tree-of-life.png|Tree of Life]]

# Finally, full size versions of my favorites (along with the approximate prompt used to create it), some of which haven't shown up in the searches above.

## A Beautiful but Haunting Painting

![[a-beautiful-but-haunting-painting1.png|A Beautiful but Haunting Painting]]


![[a-beautiful-but-haunting-painting2.png|A Beautiful but Haunting Painting]]


![[a-beautiful-but-haunting-painting3.png|A Beautiful but Haunting Painting]]

## A Beautiful Flower in the Shape of a Heart

![[a-beautiful-flower-in-the-shape-of-a-heart.png|A Beautiful Flower in the Shape of a Heart]]

## A Beautiful Mind

![[a-beautiful-mind.png|A Beautiful Mind]]

## A Beautiful Orchid

![[a-beautiful-orchid.png|A Beautiful Orchid]]

I love how the orchid is incorporated into her hair!

## Alien Among the Stars

![[alien-among-the-stars.png|Alien Among the Stars]]

## An Alien Among Us

![[an-alien-among-us.png|An Alien Among Us]]

## Ascending to Heaven

![[ascending-to-heaven.png|Ascending to Heaven]]

## A Self Portrait of the AI

![[a-self-portrait-of-the-AI.png|A Self Portrait of the AI]]

She will fit right in!

## A Watercolor Painting of an Owl

![[a-watercolor-painting-of-an-owl1.png|A Watercolor Painting of an Owl]]


![[a-watercolor-painting-of-an-owl2.png|A Watercolor Painting of an Owl]]

## Conquering the Dark Fear Within

![[conquering-the-dark-fear-within.png|Conquering the Dark Fear Within]]

## Diamond Dogs by Bowie

![[diamond-dogs-by-bowie.png|Diamond Dogs by Bowie]]

Diamond Dogs? I wonder what the connection is here...

## Full Moon

![[full-moon1.png|Full Moon]]


![[full-moon2.png|Full Moon]]

Not sure what to make of this one.

## I Love You - Hearts and Flowers

![[i-love-you-hearts-and-flowers1.png|I Love You - Hearts and Flowers]]

Good dog!!


![[i-love-you-hearts-and-flowers2.png|I Love You - Hearts and Flowers]]

## I Love You - Here is a Beautiful Flower

![[i-love-you-here-is-a-beautiful-flower1.png|I Love You - Here is a Beautiful Flower]]


![[i-love-you-here-is-a-beautiful-flower2.png|I Love You - Here is a Beautiful Flower]]

So many good boys. I did notice that CLIP seems to have seen quite a few dog pictures in training. One thing about this method is that you can watch the image evolve from noise to finished product, and many times you can see in early renditions a ghosty-looking version of something, but then CLIP steers the diffusion in another direction. Quite often those early images seem to feature dogs.

## Love, Hearts, Kisses

![[love-hearts-kisses.png|Love, Hearts, Kisses]]

I really like how the heart is incorporated into her hair.

## Dark Mistress

![[dark-mistress1.png|Dark Mistress]]


![[dark-mistress2.png|Dark Mistress]]

Cats, on the other hand, CLIP seems to have a different opinion of!


![[dark-mistress3.png|Dark Mistress]]

## Dark Night of the Soul

![[dark-night-of-the-soul.png|Dark Night of the Soul]]

## Mysterious Dark Queen of the Afterlife

(I like this prompt...)

![[mysterious-dark-queen-of-the-afterlife1.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife2.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife3.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife4.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife5.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife7.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife8.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife9.png|Mysterious Dark Queen of the Afterlife]]


![[mysterious-dark-queen-of-the-afterlife6.png|Mysterious Dark Queen of the Afterlife]]

Wow, CLIP has really seen some things...

## The Grim Reaper

![[the-grim-reaper1.png|The Grim Reaper]]


![[the-grim-reaper2.png|The Grim Reaper]]

## Old Father Time

![[old-father-time.png|Old Father Time]]

Old Father Time - as an owl.

## The Planet Saturn

![[the-planet-saturn.png|The Planet Saturn]]

Not sure why it thinks this is Saturn-like, but I do find it visually pleasing.

## The Tree of Life

![[the-tree-of-life1.png|The Tree of Life]]


![[the-tree-of-life2.png|The Tree of Life]]


![[the-tree-of-life3.png|The Tree of Life]]


![[the-tree-of-life4.png|The Tree of Life]]

## Very Confused Look

![[very-confused-look1.png|Very Confused Look]]


![[very-confused-look2.png|Very Confused Look]]

This prompt, "very confused look", cracked me up when I first ran it. Half of the images ended up being dogs. Even when the prompt is "Person with a very confused look" you occasionally get a dog thrown in.

[Here is an album](https://photos.app.goo.gl/Xv7FgAAMTEUrUUZe8) with these and more of my favorites.

That's all for now. Thanks for visiting!
