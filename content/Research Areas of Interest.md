---
title: Research Areas of Interest
draft: true
tags: 
date: 2024-02-02
---
 Advancing the capabilities of current systems (DL and other), especially where real weaknesses exist:
- The biggies:
	- 1. Multimodal, spatiotemporal (time + 3D) representation of knowledge / understanding
	- 2. World models and structured thinking
	- 3. Intersection of Neuroscience and AI (SNNs, predictive coding, etc.)
- Other stuff:
	- Generative models
	- Reservoir computing / FNet implications and ties to cortex mini-colums and 'units of computation / pattern recognition'
	- Sample / data inefficiency
	- Grounding (in both the real world and across modalities)
	- Reasoning / Causal reasoning
	- Diffusion as a generative process

Bringing learnings from neuroscience, linguistics, and our understanding of the human brain to bear on AI / ML
- 'Structured thinking' / world models / predictive coding
- Neurological inspirations, like spiking models of the neuron
- The free energy principle
- Grounding in the physical and temporal world / embodiment
- Sparsity
- Experience replay
- Attention

Other:
- Democratization of AI / ML technologies and ensuring that capabilities remain accessible to smaller organizations
- Bias issues, safety issues, privacy issues

## to merge with above

- Extending the context length of LLMs:
	- Architectural approaches like Mamba, MoE-Mamba / BlackMamba.
	- Methodological approaches like MemGPT and RAG-like approaches. Function calling plays a role here.
- Reasoning, System 2 thinking, rumination / pondering: related to some of the other items here, esp agenticity.
	- I also keep coming back to the notion of wanting a system that has feedback, and maybe 'settles' to a solution (which allows it to take more or less time, depending on the scenario).
- Agenticity, planning, acting.
- Mechanistic interpretability.
- Multimodality.
	- Common latent spaces.
	- VMamba, Vision Mamba and similar. Would be very interesting to try MoE-Mamba on vision. And combining token-free (byte-based) Mamba with vision.
- Biological inspirations.
	- Fovea / Ventral & Dorsal streams.
	- Feedback loops. There are a few ties here to conventional architectures / approaches. For example, to what extent are normal transformers mimicking feedback loops, via information that morphs through the layers
- Doing more with low resources
	- Local LLama and the like
	- Model merging
	- TinyStories. Curriculum learning (check out [BabyLM](https://babylm.github.io/))
	- LoRA and QLoRA
	- MoE
	- Mamba / MoE-Mamba / BlackMamba fit in here as well
	- Adaptive / conditional computation (adding more computation when needed for the problem at hand)
- Misc
	- Vec2Text methods (including my [[Vec2Text LM]] idea)
