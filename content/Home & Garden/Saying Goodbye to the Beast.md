---
title: Saying Goodbye to the Beast
draft: false
tags:
  - post/home-garden
date: 2024-06-15
promo-linkedin:
---
One of my hobbies in the late '80s / early 90s was designing and building audio equipment.

It was a nice fit for a newly-minted electrical engineer who was really interested in analog signal processing (this was just around the time that digital signal processing was taking off, but it wouldn't be viable for consumer-grade electronics until later). For me it was pre-kids, when you seemingly have all the time in the world to devote to hobbies.

I considered myself a bit of an audiophile, and progressed through a few amplifier and speaker projects that grew in scope and ambition, in search of the ultimate stereo. My quest culminated with a system built around a splitter + amplifier I call 'the Beast'. It was designed to partner with a monster pair of (also custom-designed and built) speakers. It was a project of some passion; I spent many hours designing and testing the setup (at one point even writing software that used recorded impulse responses to model the entire system in the acoustics of a specific room).

Here's the Beast:

![[the-beast.png]]

Some noteworthy aspects:
- It uses active frequency filtering. Virtually all consumer speakers use passive filtering, which is easier to implement but has limitations. The active approach allowed me to tune the filters to individual speaker components and to experiment with different cutoffs (frequency, number of poles, etc.) in a way that wasn't readily feasible with passive filters. The active filtering approach has a couple of major drawback, however: 1) it couples the speakers directly to the amp setup (that is, you need the two to be co-designed) 2) you need one amp per speaker driver (instead of one for a speaker containing several drivers). These drawbacks are why you don't see this approach taken in the consumer space.
- All the electronics were custom designed and hand assembled, including etched amplifier boards.
- Everything was optimized for linearity (which comes at a cost of efficiency; that thing ran quite hot).
- Much of the hardware was surplus, scrounged at low cost from a couple of electronics stores I used to frequent.
- The thing is massive—literally. *Over 50 pounds!* Most of the weight is from the monster transformers in the power supplies.

The Beast, and the speakers it was paired with, served me well for a number of years. But at one point almost two decades ago the (commercial) pre-amp that operated upstream of the Beast died. In what I told myself was a temporary move (until I could find a suitable replacement for the pre-amp), I pulled the Beast and its speakers out of the living room and relegated them to storage in the garage. I hooked up the rest of my components to a more modest (conventional) amp / speaker combo.

Fast forward a while. As life went on—kids arriving and then leaving, with the Beast and its speakers gathering dust in the garage—my need to have a ridiculously over-powered stereo system faded (I grew up??).

Now my wife and I are prepping to finally—for real this time!—clean out all the crap that has accumulated in our garage since moving into this house many years ago. I've decided it's time to let go of the Beast and its speakers. I'm allowing myself a kind of parting ceremony with this old labor of love by documenting it here.

Here's the back of the pair of cases. Power supplies in the bottom case, active filtering and amplifiers in the top. Lots of DC running from bottom to top (for each set of amps).


![[back-panel.png]]


This is the inside of the top case, which handles the audio. There are a pair of amps for each driver in the speakers (one for left speaker, one for right). This is where we differ from a conventional setup, which sends one signal to each speaker, and then uses passive filtering to split the signal between drivers.

The active filtering is on the left (on cheesy breadboards that I never got around to cleaning up). The speaker amps are middle and right side. The fans on the right do their best to keep the thing at a reasonable temp.

![[amplifiers.png]]


This is the underside of one of the amps on the right side of the pic above. It has hand-wound wood-core inductors and other stuff on a simple circuit board I designed and etched myself (after testing out breadboard prototypes). My soldering was functional but not pretty!

![[circuit-board.png]]


Here's the inside of the bottom case, which contains the power supplies for the amps. Lots of transformer iron together with scary-big capacitors (I was always a bit nervous working around those things). I had to brace the case with extra mechanical support to handle the weight (~35 lbs).

![[power-supplies.png]]


![[power-supplies-2.png]]

Schematic for some of the electronics:

![[schematic.png]]

PCB design for the amp:

![[amp-pcb.png]]

Here's the speaker enclosure design:

![[speaker-diagram.png]]

Endless tweaking of filter and speaker response curves:

![[response-curves.png]]

Playing around with a setup to use the FFT of impulse responses to measure speaker driver + enclosure + room characteristics—a cool end-to-end learning experience involving hardware and my own software. I don't even remember what language the anaysis code was written in... Basic? Pascal?

![[impulse-fft.png]]

That's it!

As noted above, the Beast is not useful except when married to its matching speakers, and those speaker cones have started to disintegrate (and I never got around to finishing the enclosures anyway). At this point I would hesitate to even power it up for fear of something blowing.

Next: figure out what, if anything, can be salvaged here, aside from a bunch of iron and copper.

Adios, old friend.
