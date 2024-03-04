---
title: Structured Thinking
draft: false
tags: 
date: 2022-12-03
---
Repo: There's no chance this code will be made public; just thinking about that gives me the shakes. Because I was coming down a bunch of learning curves at once, and was working on this exercise on nights and weekends only, it meandered over several months in a barely coherent fashion. And at the time I did not understand how to inherit from Hugging Face classes, so instead copied large swaths of the HF code and modified it. Madness!

## The Idea

This was my first real foray into munging some data and into doing surgery on a model (the patient barely survived!) in order to try out an idea I had.

This was just around the time that LLMs were starting to take off; it was still the era of using BERT and friends for NLP tasks. My thinking was that models like BERT might benefit from having an inductive bias towards a structure in their latent space, and that perhaps we could nudge them in the right direction by injecting some helpful ancillary data along with their main input.

After stepping back from many over-ambitious plans that I had no hope of executing (with my rudimentary skills), I came up with something more modest that I considered worth attempting. I would pre-process input data with a standalone tool (the wonderful [spaCy](https://spacy.io)) to extract some grammatical info about the input text, and then inject that information straight into the veins of the model (I chose DistilBERT) to see how performance was affected.

Here's a diagram showing dimensions of a single input to (vanilla) DistilBERT:

![[transformer-embedding-encoding-dim.png]]

The idea was to modify this to also input grammatical information about the input tokens, as in this diagram:

![[transformer-sent-diag-embedding-encoding-dim.png]]

The three new fields, POS, DEP, and RHP are based on spaCy's sentence diagram capabilities:

- POS: Part of Speech
- DEP: Dependency, the syntactic relation connecting child to head
- RHP: Relative Head Position, the (relative) position of the part-of-speech tag of the token head

I created a little dataset based on Flickr-8k, which consists of a set of photos together with multiple (human-generated) captions for each. For this work I ignored the photos and created pairs of randomly-selected captions. The task was to predict whether or not the two captions corresponded to the same photo.

Here's a positive example:

```python
{'cap1': 'A man and a woman walk their dogs on leashes .',
 'cap2': 'Dogs straining on leashes towards each other , as owners walk apart on grass .',
 'label': 1}
```

Here's a negative:

```python
{'cap1': 'An old man in a black coat and hat leans against a brick building .',
 'cap2': 'Tall trees reach to the horizon as a cyclist navigates the way through the tangled roots .',
 'label': 0}
```

Let's take that second caption above: "Dogs straining on leashes towards each other , as owners walk apart on grass ." Here's the resulting sentence diagram from spaCy:

![[Pasted image 20240303101038.png]]

And this table shows the corresponding diagrammatic info that we feed into the model to help it out:

```
I_pos  Text           | POS      Dep      Head    Rel Head Pos
==============================================================
0      Dogs           | NOUN     nsubj    1       1
1      straining      | VERB     ROOT     1       0
2      on             | ADP      prep     1       -1
3      leashes        | NOUN     pobj     2       -1
4      towards        | ADP      prep     1       -3
5      each           | DET      det      6       1
6      other          | ADJ      pobj     4       -2
7      ,              | PUNCT    punct    1       -6
8      as             | SCONJ    mark     10      2
9      owners         | NOUN     nsubj    10      1
10     walk           | VERB     advcl    1       -9
11     apart          | ADV      advmod   10      -1
12     on             | ADP      prep     10      -2
13     grass          | NOUN     pobj     12      -1
14     .              | PUNCT    punct    1       -13
```

Some interesting side learnings:
- When you tokenize that sentence some of the words get split up in the usual manner, so there's a little bit of management to keep the word-level information tied to the appropriate tokens.
- In order to use the pretrained DistilBERT (with some fine-tuning), I used PCA to do the reduction of embedding matrices from 768 to 672 (in the diagrams above). I also experimented with UMAP.

## The Experiment


## Results


## Takeaways

(#quite naive about capabilities of models and how they learn#)

## Additional Thoughts

