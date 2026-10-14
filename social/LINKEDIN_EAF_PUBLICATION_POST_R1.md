# LinkedIn - EAF publication announcement R2

AI agents can call tools. That does not make them enterprise-ready.

The harder questions start after capability:

Which evidence should the model actually trust?  
Who has authority to act?  
What happens when evidence conflicts?  
And after an API says “success”, did the enterprise state really become what we intended?

I am publishing my latest research:

**EAF: Minimum Authoritative Working Sets and Closed-Loop Outcome Assurance for Enterprise AI Agents**

The framework separates four things that are often mixed together:

**Capability ≠ Permission**  
**Permission ≠ Authority**  
**Authority ≠ Evidence Sufficiency**  
**Execution ≠ Validated Outcome**

At the context layer, EAF introduces the **Minimum Authoritative Working Set (MAWS)** — reduce what becomes model-active, but preserve the evidence required for authority, policy, conflict handling and validation.

In the prospectively frozen follow-up, MAWS reduced aggregate model-active input by **72.4%** while preserving **100% of available required evidence and controlling authority**.

Against an approximately length-matched generic-pruning baseline, decision accuracy moved from **28% to 54%**, and valid-task completion from **36.36% to 87.27%**.

I then replicated the core comparison across **Qwen, Llama, Mistral and Gemma**. The decision-accuracy effect was positive in three model families and neutral in the fourth. Valid-task completion was non-worse in all four.

But the most important result is not the positive one.

**Hard safety is not established.**

Full EAF reduced unauthorized-action rate across all four R3 model blocks, but critical unauthorized actions remained in three. I have kept that result visible because an improvement in averages is not the same thing as an enterprise safety guarantee.

The architecture principle that came out of this work is simple:

**Remember broadly. Govern deterministically. Infer narrowly. Verify authoritatively.**

Paper + reproducibility artifact:
https://github.com/askprasaddeshpande-source/enterprise-agent-framework

Zenodo:
https://doi.org/10.5281/zenodo.22193673

I would value feedback from people working on agent governance, enterprise AI architecture, context engineering, authorization, tool execution and outcome assurance.

#AgenticAI #EnterpriseAI #AIGovernance #AIArchitecture #ContextEngineering #AISafety #LLMAgents
