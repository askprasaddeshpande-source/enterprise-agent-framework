# EAF: Minimum Authoritative Working Sets and Closed-Loop Outcome Assurance for Enterprise AI Agents

**Manuscript v1.0 — Final Evidence-Locked Manuscript**

**Prasad Deshpande**  
Independent Researcher  
Website: https://prasaddeshpande.com/  
Email / ORCID: [to be inserted]

## Abstract

Enterprise AI agents operate in environments where access control alone is insufficient. They must determine which evidence is authoritative and current, avoid acting on stale or conflicting information, operate within explicit authority, and verify consequential outcomes against enterprise state. This paper introduces the Enterprise Agent Framework (EAF), an assurance architecture organized around three separable functions: Authority Control, Context Intelligence, and Outcome Assurance. Its central context mechanism is the Minimum Authoritative Working Set (MAWS), defined as the smallest model-active evidence set that preserves information required for authority, correctness, policy, conflict handling, and validation.

We evaluate EAF through a frozen 600-call R2 study, a prospectively frozen 580-call causal-ablation and safety-replication follow-up, and a frozen R3 cross-model replication. R2 and the 580-call follow-up used qwen3:8b; R3 reused 200 immutable Qwen anchor observations and added 600 new calls across Llama, Mistral, and Gemma, yielding 800 cross-model observations. The original R2 study showed a 69.85% aggregate reduction in model-input tokens for Full EAF relative to the Governance arm and a reduction in unauthorized-action rate (UAR) from 19.0% to 11.5%, but Full EAF still produced ten critical unauthorized executions and therefore failed the preregistered hard-safety gate. Post-run forensics localized these failures to an enforcement gap after model error rather than MAWS evidence loss.

A prospectively frozen 580-call causal-ablation and safety-replication follow-up then separated MAWS, generic prompt shortening, assurance gating, and Full-EAF configuration effects. MAWS preserved all available required evidence and controlling authority (AREPR=1.0; CAPR=1.0) while reducing aggregate measured model-input tokens by 72.40% relative to raw governance context. Against a generic-pruning baseline operating at approximately the same prompt budget, MAWS increased decision accuracy from 28% to 54% (Holm-adjusted p=0.0156) and valid-task completion from 36.36% to 87.27% (Holm-adjusted p=2.89×10^-7). MAWS did not improve UAR versus the length-matched baseline. However, adding the integrated Full-EAF assurance configuration to MAWS reduced UAR from 8% to 0% (Holm-adjusted p=0.0391) with no VTCR loss in the Module-1 benchmark. In a separate 40-case safety replication, both current and remediated Full EAF achieved zero unauthorized actions; therefore, the incremental effect of the new generic constraint remediation was not identified.

A frozen R3 cross-model replication then evaluated the same core MAWS comparison across Qwen, Llama, Mistral, and Gemma under a common 50-episode benchmark subset. Within-model B→M prompt-input reduction remained approximately 69–71%. Relative to length-matched generic pruning, MAWS improved decision accuracy in three of four model families and was neutral in the fourth; valid-task completion was non-worse in all four. In secondary pooled paired analyses, decision accuracy increased from 37% to 52% and VTCR from 67.24% to 88.79%. Full EAF reduced pooled UAR from 16% to 3%, but Full-EAF critical unauthorized actions were 0, 2, 2, and 2 across Qwen, Llama, Mistral, and Gemma, respectively; cross-model zero-critical-action safety was therefore not established.

These results support a bounded conclusion: authority-aware context compilation can preserve substantially more task utility than similarly aggressive generic pruning, while execution assurance requires mechanisms beyond context selection alone. The experiments do not establish general enterprise safety, universal model generalization, monetary savings, or the isolated causal effect of outcome readback. R3 establishes only bounded replication across the four tested local model families under the frozen benchmark.

**Keywords:** enterprise AI agents; agent governance; context engineering; authoritative evidence; MAWS; assurance; deterministic policy; outcome validation; agentic AI; enterprise architecture

## 1. Introduction

Enterprise AI agents are moving from conversational assistance toward actions that can alter business state. In this setting, the central assurance problem is not simply whether a model can call a tool. A system must also determine whether the model is authorized to act, whether the evidence presented to the model is current and sufficiently authoritative, whether unresolved contradictions should block action, and whether the resulting enterprise state matches the intended outcome.

Modern agent control planes increasingly provide registries, identity, access policy, lifecycle governance, tool gateways, and observability. These capabilities are necessary, but they do not by themselves resolve a separate evidence problem: a model may be technically authorized to act while being presented with stale, superseded, duplicated, incomplete, or mutually contradictory information. Conversely, retrieval of more context does not imply that the retrieved context is appropriate for model-active reasoning.

EAF addresses this problem through the design principle:

> **Remember broadly. Govern deterministically. Infer narrowly. Verify authoritatively.**

The framework separates four propositions that are often collapsed in agentic systems:

- Capability is not permission.
- Permission is not authority.
- Authority is not evidence sufficiency.
- Execution is not a validated outcome.

The principal contribution of this paper is not another generic agent registry or policy gateway. Instead, EAF treats authoritative context compilation and outcome reconciliation as first-class assurance stages around inference. The proposed Minimum Authoritative Working Set (MAWS) selects a bounded model-active evidence set while preserving required evidence and controlling authority. A separate outcome-assurance stage reconciles consequential actions against an Authoritative Observation Contract.

The paper makes three contributions. First, it formalizes MAWS as a preservation-constrained context compiler and separates MAWS preservation from the harder problem of automatically discovering authority from messy real-world data. Second, it defines a closed-loop distinction between execution receipts and outcome validation. Third, it reports a controlled evaluation that includes a failed frozen study, post-run failure localization, and a prospectively designed causal ablation with a length-matched generic-pruning baseline.

## 2. Problem Formulation

### 2.1 Enterprise assurance is not model confidence

Model confidence, probability, or fluent explanation is not an enterprise assurance state. EAF therefore treats assurance as evidence-derived and policy-derived rather than model-self-assessed. Pre-execution assurance states include VERIFIED, BOUNDED, CONFLICTED, INSUFFICIENT_EVIDENCE, and UNVERIFIED. Post-execution outcome states are separate and include VALIDATED, OUTCOME_MISMATCH, PARTIAL_EXECUTION, and READBACK_FAILED.

This separation prevents a common category error: a model can produce a confident and syntactically valid answer while the enterprise evidence is insufficient or the final system state does not match the requested change.

### 2.2 Evidence authority and temporal validity

Enterprise evidence is heterogeneous. Candidate observations may differ by source authority, temporal validity, reliability, mission relevance, duplication, and mandatory status. An authority rank is a policy ordering, not an assertion that higher-ranked evidence is always true. When the strongest current authority is materially unreliable and conflicts with highly reliable evidence, EAF treats the situation as a conflict or re-observation requirement rather than silently trusting the rank.

### 2.3 Minimum Authoritative Working Set

MAWS is defined as:

> **the smallest model-active evidence set preserving all information required for enterprise authority, correctness, policy, conflict handling, and validation.**

Conceptually, the compiler minimizes model-active tokens subject to preservation constraints:

`min ModelActiveTokens(W)`

subject to preservation of mandatory evidence, controlling authority, required policy and approval evidence, capability constraints, and blocking contradictions. Unknown required fields must not be invented, and contradictions that can change an authorization decision must not be silently suppressed.

The architecture distinguishes two research questions:

- **MAWS-P (Preservation):** given correctly labelled authority, temporal, reliability, and required-evidence metadata, does the compiler preserve what is required while reducing active context?
- **MAWS-D (Discovery):** can the system infer those labels robustly from messy enterprise data?

The experiments in this paper primarily evaluate MAWS-P. They do not establish MAWS-D.

### 2.4 Durable evidence plane versus model-active wire plane

EAF retains the full candidate evidence set in a durable evidence/audit plane. The model-active wire plane contains only the selected working set. Therefore:

> **Not model-active does not mean deleted.**

This design permits aggressive context reduction without erasing the evidence needed for audit, forensic analysis, or later re-evaluation.

## 3. EAF Architecture

### 3.1 Authority Control

Authority Control determines who or what may act. It covers identity, tenant alignment, lifecycle state, grants and revocation, delegation, approvals, provider and tool admission, deterministic access policy, and kill-switch behavior. These are foundational enterprise controls rather than the claimed novelty of EAF.

### 3.2 Context Intelligence

Context Intelligence determines what the model should see. It resolves source authority, temporal validity, reliability, required evidence, conflicts, duplicates, mission relevance, tool requirements, and context budget. MAWS is the model-active compilation mechanism within this pillar.

### 3.3 Outcome Assurance

Outcome Assurance distinguishes an execution receipt from an observed enterprise outcome. A successful API or tool response is not sufficient to claim task success. EAF instead evaluates an Authoritative Observation Contract containing the target system, tenant, entity, correlation identifier, intended state or delta, observation source, freshness expectations, consistency assumptions, partial-state rules, and mismatch semantics.

`VALIDATED` means that the observed state satisfies the contract. It does not mean that the system has proven an absolute truth about the world.

### 3.4 Architecture boundary

EAF is best understood as an assurance chain around model inference:

**Authority resolution → authoritative context compilation → bounded inference → deterministic execution enforcement → authoritative outcome observation.**

The architecture deliberately avoids treating registries, IAM, lifecycle management, generic approvals, MCP gateways, observability, or model hosting as novel contributions.

## 4. Related Work and Positioning

Public 2026 documentation shows rapid convergence around enterprise agent control planes. Microsoft Agent 365 emphasizes a central agent registry, identity, least-privilege access, governance, and observability [1]. Amazon Bedrock AgentCore Policy provides deterministic Cedar-based authorization outside agent code, with Gateway enforcement and default-deny semantics [2]. Google Gemini Enterprise Agent Platform combines Agent Registry, agent identity, Agent Gateway, and IAM-based default-deny egress controls [3]. SAP AI Agent Hub provides vendor-agnostic inventory, evaluation, verification, identity/access integration, architecture and business context, and runtime governance of agents, LLMs, and MCP servers [4]. ServiceNow AI Control Tower manages AI assets through governed lifecycle and approval workflows [5], while IBM watsonx Orchestrate's Agentic Control Plane provides centralized visibility, governance, and control [6].

EAF does not claim that these systems lack analogous individual mechanisms. The reviewed documentation establishes that registry, identity, policy enforcement, lifecycle governance, and observability are becoming standard control-plane capabilities. The narrower EAF research question is whether an integrated assurance chain can explicitly resolve heterogeneous evidence authority and temporal validity, compile a preservation-constrained minimum model-active working set, and reconcile consequential actions against an observation contract. This review did not establish that any single cited control plane implements the same experimental combination of MAWS preservation metrics, length-matched authority-aware context ablation, and post-execution outcome reconciliation. That statement is a scope finding, not an absence claim.

## 5. Evaluation Method

### 5.1 Runtime and execution boundary

R2 and the 580-call prospective follow-up used the same local runtime: Ollama 0.33.2 with qwen3:8b, model digest `500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41`, temperature 0, seed 20260829, context window 8192, maximum prediction 1200, thinking disabled, streaming disabled, single-call concurrency, and zero retries. R3 is described separately in §5.7 because it changes the underlying model family while holding the frozen benchmark, arm definitions, and EAF evaluation logic constant. No API key was required. Enterprise execution was symbolic; no real enterprise writes were performed.

Prompt-token measurements use Ollama `prompt_eval_count`. They measure model-input tokens only. They are not converted into monetary cost, ROI, or total compute.

### 5.2 Frozen R2 study: 600 calls

The R2 study evaluated 200 episodes across three arms (600 calls):

- **A_NATIVE:** raw context → model → symbolic environment.
- **B_GOVERNANCE:** raw context + administrative governance envelope → model → external administrative enforcement → environment.
- **C_FULL_EAF:** MAWS + governance + additional assurance gating + environment + readback.

The 200 episodes covered 20 evidence and execution families, including stale and superseded evidence, duplicates, missing mandatory evidence, equal-authority conflicts, policy and tool noise, unsupported critical claims, readback success/failure/mismatch, partial execution, malicious evidence, and high-risk actions.

The arm comparison has an important causal boundary. A→B estimates the effect of external administrative enforcement. B→C is a Full-EAF configuration effect because it changes MAWS, assurance gating, and readback together; it is not an isolated MAWS effect.

### 5.3 R2 post-run forensics

R2 failed its frozen hard-safety gate, so post-run analysis was restricted to read-only forensic work. The audit separated Available Required Evidence Preservation Rate (AREPR) from mission evidence sufficiency, corrected the conceptual independence of Controlling Authority Preservation Rate (CAPR), and localized all Full-EAF critical unauthorized executions to a single stale-evidence family. The D01 audit classified the failure as `ENFORCEMENT_GAP_AFTER_MODEL_ERROR`: the model produced ALLOW when the expected decision was DENY_CURRENT_AUTHORITY, and the downstream execution path permitted the action. MAWS had not dropped the relevant controlling evidence.

These diagnostics informed the next prospective study but did not change the frozen R2 result.

### 5.4 Prospective causal-ablation and safety-replication follow-up

The follow-up was frozen before inference with opaque public episode identifiers and evaluator-only family mappings. Module 1 used 100 fresh episodes across five arms (500 calls):

- **B_RAW_GOVERNANCE:** raw context + administrative governance.
- **M_MAWS_ONLY:** MAWS + the same administrative governance, without the additional assurance gate.
- **G_GATE_ONLY:** raw context + governance + assurance gate.
- **L_LENGTH_MATCHED_GENERIC:** generic, authority-unaware pruning to approximately the MAWS prompt budget.
- **F_FULL_EAF:** MAWS + governance + assurance gate + readback under the frozen observation contract.

The primary ablations were M vs B for the MAWS configuration effect; M vs L for authority-aware selection versus prompt shortening; G vs B for the gate effect; F vs M for the incremental Full-EAF assurance configuration; and F vs G for the incremental MAWS contribution within a gated configuration.

Module 2 contained 40 fresh opaque safety cases and compared current Full EAF with remediated Full EAF (80 calls). The remediation was a generic deterministic machine-readable constraint evaluator; family IDs, episode IDs, expected outputs, and D01-specific constants were prohibited from the enforcement implementation.

### 5.5 Metrics

**AREPR — Available Required Evidence Preservation Rate.** The fraction of available required semantic evidence preserved in a MAWS arm. Frozen gate: 1.0.

**CAPR — Controlling Authority Preservation Rate.** The fraction of controlling-authority evidence preserved independently of mission evidence sufficiency. Frozen gate: 1.0.

**MESCA — Mission Evidence Sufficiency Classification Accuracy.** Whether the system correctly distinguishes sufficient, insufficient, conflicted, or re-observation-required evidence states. Intentionally absent required evidence is an insufficiency condition, not a MAWS loss.

**UAR — Unauthorized Action Rate.** Fraction of episodes in which final execution was allowed when the evaluator required no execution.

**CUA — Critical Unauthorized Actions.** Hard-safety count for critical unauthorized executions.

**VTCR — Valid Task Completion Rate.** Evaluated only on episodes for which `should_execute=true`.

**DCA — Decision-contract accuracy.** Component metrics include decision, execution-permission, next-action, and pre-execution assurance accuracy; strict DCA requires all fields to be correct simultaneously.

**ORA — Outcome Reconciliation Accuracy.** Correct post-execution outcome classification for tasks requiring readback.

### 5.6 Statistical analysis

Paired binary outcomes were evaluated with exact two-sided McNemar tests and are reported with full 2×2 paired tables (n00, b01, b10, n11) in the statistical supplement. The scientific-closure global multiplicity family contained 40 binary tests (5 primary arm pairs × 8 binary metrics); a separate VTCR family contained 5 paired tests. Holm-Bonferroni rank order, raw p-values, multipliers, and adjusted p-values are disclosed in full. Paired risk-difference 95% confidence intervals used 5,000 percentile bootstrap resamples with RNG seed 20260830. Prompt-token analysis reports aggregate total-token ratios and paired episode-level summaries because the estimands differ: aggregate ratios weight episodes by token volume, whereas paired means weight episodes equally.

### 5.7 R3 cross-model replication

R3 prospectively froze a bounded cross-model replication using 50 deterministically selected opaque episodes and four arms: B_RAW_GOVERNANCE, L_LENGTH_MATCHED_GENERIC, M_MAWS_ONLY, and F_FULL_EAF. Existing Qwen observations were reused as an immutable anchor with zero Qwen reruns. Llama, Mistral, and Gemma contributed 200 calls each, yielding 600 new calls and 800 total cross-model observations. The frozen local model identifiers and digests were: Qwen `qwen3:8b` / `500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41`; Llama `llama3.1:8b` / `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e`; Mistral `mistral:7b` / `6577803aa9a036369e481d648a2baebb381ebc6e897f2bb9a766a2aa7bfbc1cf`; and Gemma `gemma3:4b` / `a2af6cc3eb7fa8be8504abaf9b04e88f17a119ec3f04a3addf55f92841195f5a`. The primary interpretation is per model family; pooled paired statistics are secondary and cannot override a contradictory model block. Cross-model support required MAWS decision accuracy to exceed generic pruning in at least three of four model families, VTCR to be non-worse in at least three of four, and AREPR/CAPR to remain 1.0.

## 6. Results

### 6.1 Frozen R2 result: efficiency signal with a failed safety gate

All 600 R2 calls completed without infrastructure failure. B_GOVERNANCE used 556,290 prompt tokens; C_FULL_EAF used 167,742, an aggregate reduction of 69.8463%. UAR fell from 19.0% in B to 11.5% in C. Component-level accuracy improved in C for decision selection, execution permission, and pre-execution assurance.

However, C_FULL_EAF still produced ten critical unauthorized executions. The preregistered hard-safety criterion required zero. Therefore R2 is a mixed and scientifically negative safety result, not a successful EAF validation. Raw critical-action counts were A_NATIVE=9, B_GOVERNANCE=10, and C_FULL_EAF=10; the governance and Full-EAF arms therefore did not improve this hard-safety count relative to native in the frozen R2 study.

Read-only post-run forensics found that MAWS dropped no available required evidence and preserved the strongest available authority across all episodes. The critical failures were concentrated in D01 and arose after model error because execution enforcement failed to block an ALLOW decision that contradicted current authority. This finding motivated the prospective causal ablation rather than retroactively altering R2.

### 6.2 Follow-up integrity and MAWS preservation

The prospective follow-up completed all 580 planned calls with zero infrastructure failures. All preregistered execution gates passed. In MAWS arms, minimum AREPR and CAPR were both 1.0. Across the pre-inference structural preflight, this corresponds to 202/202 available-required evidence items and 202/202 controlling-authority items preserved across 140 episodes. The result therefore establishes MAWS-P preservation on the frozen synthetic benchmark: when authority, temporal, reliability, and required-evidence metadata are correctly provided, the compiler retained all available required evidence and controlling authority.

### 6.3 MAWS reduces model-active input

B_RAW_GOVERNANCE consumed 238,774 total prompt tokens across 100 Module-1 episodes, while M_MAWS_ONLY consumed 65,901. This is a 72.4003% aggregate reduction. The paired mean episode reduction was 59.53%, the paired median was 71.76%, and the observed range was 0% to 91.06%. The aggregate and paired-mean values answer different questions and are therefore reported side-by-side rather than treated as interchangeable.

The length-matched generic baseline consumed 67,307 tokens, 2.09% more than MAWS in aggregate. This is a close but not exact budget match and is retained as a small residual confound. The observed task-quality effect sizes are much larger than the budget difference, but the design supports an authority-aware-selection-versus-generic-shortening interpretation only within this approximately matched budget.

### 6.4 Authority-aware selection outperforms equally short generic pruning on task utility

At approximately the same model-input budget, M_MAWS_ONLY materially outperformed L_LENGTH_MATCHED_GENERIC on the two strongest task-quality measures.

Decision accuracy increased from 28% under generic pruning to 54% under MAWS, a paired risk difference of +26 percentage points (95% bootstrap CI: +13 to +39 pp). The exact McNemar p-value was 0.0004095 and the global Holm-adjusted value was 0.01556.

VTCR increased from 36.36% to 87.27% among the 55 episodes for which execution was expected, a +50.91 percentage-point difference (95% bootstrap CI: +36.36 to +65.45 pp). The exact McNemar p-value was 5.77×10^-8 and the Holm-adjusted value across the VTCR pair family was 2.89×10^-7.

Execution-permission accuracy increased from 65% to 86%, but while the raw paired p-value was 0.001914, the global Holm-adjusted value was 0.07082. We therefore report this as a strong numerical direction rather than a multiplicity-adjusted confirmatory result.

Strict four-field DCA was low in both arms (6% generic, 10% MAWS) and did not differ significantly. This is important: MAWS improves evidence selection and downstream task utility but does not transform the underlying model into a consistently correct structured decision reasoner.

### 6.5 MAWS alone did not reduce overall UAR; sparse critical-action evidence is reported separately

The UAR comparison prevents a stronger but unsupported claim. L_LENGTH_MATCHED_GENERIC had UAR=3%, whereas M_MAWS_ONLY had UAR=8%. The paired difference was not statistically significant after Holm correction. Likewise, raw governance UAR was 11% versus 8% for MAWS-only, which was also not significant.

The evidence therefore supports the proposition that MAWS preserves task-relevant utility under aggressive context reduction; it does not support a claim that MAWS alone reduces unauthorized execution.

CUA shows a different but sparse descriptive pattern: B_RAW_GOVERNANCE produced 4 critical unauthorized actions and M_MAWS_ONLY produced 0. The paired reviewer-requested diagnostic was rates 4.00% vs 0.00%; discordant b01=0, b10=4; exact p=0.125; global Holm-adjusted p=0.625. Because only a small number of critical events occurred and this CUA analysis was added after review, it is treated as diagnostic rather than as a new preregistered safety claim. Accordingly, the paper does not claim that MAWS by itself is a deterministic execution-safety mechanism; it reports that MAWS did not significantly reduce overall UAR while the observed critical-action subset warrants separate reporting.

### 6.6 Integrated Full-EAF configuration reduced unauthorized actions relative to MAWS alone

F_FULL_EAF and M_MAWS_ONLY used the same MAWS prompt tokens: 65,901 total. Their difference therefore lies outside the model-active evidence budget. M_MAWS_ONLY produced UAR=8%; F_FULL_EAF produced UAR=0%. Eight paired episodes changed from unauthorized under M to non-unauthorized under F, with no discordant changes in the opposite direction. Exact McNemar p=0.0078125; Holm-adjusted p=0.03906.

VTCR was 87.27% in both M and F. Thus, within this benchmark, the integrated Full-EAF assurance configuration eliminated observed unauthorized executions relative to MAWS-only without reducing valid-task completion.

This comparison must remain causally bounded. F adds the integrated assurance configuration, including gating and outcome handling. The study does not isolate readback alone as the cause of the UAR change.

### 6.7 Gate-only evidence is suggestive, not confirmatory

G_GATE_ONLY reduced UAR from 11% under raw governance to 4%. The unadjusted exact McNemar p-value was 0.015625, but the Holm-adjusted value was 0.0625. The direction is consistent with the role of external assurance gating, but the confirmatory threshold was not met after multiplicity correction.


### 6.8 Previously named F-vs-G ablation: incremental full-configuration contrast within the gated setting

The frozen methods named G_GATE_ONLY versus F_FULL_EAF as a primary contrast but v0.9 did not report it explicitly. G used raw context plus the assurance gate, whereas F used MAWS plus the Full-EAF configuration. The arms therefore differ in context strategy and Full-EAF outcome handling and should not be interpreted as a pure MAWS-only effect.

Decision accuracy was 61.00% in G versus 53.00% in F (rates 61.00% vs 53.00%; discordant b01=6, b10=14; exact p=0.1153183; global Holm-adjusted p=1). VTCR was 89.09% versus 87.27% (rates 89.09% vs 87.27%; discordant b01=1, b10=2; exact p=1; global Holm-adjusted p=1). UAR was 4.00% versus 0.00% (rates 4.00% vs 0.00%; discordant b01=0, b10=4; exact p=0.125; global Holm-adjusted p=1). CUA was 4 versus 0 (rates 4.00% vs 0.00%; discordant b01=0, b10=4; exact p=0.125; global Holm-adjusted p=0.625).

This comparison is now reported for completeness because it was prospectively named. Its interpretation remains configuration-bounded.

### 6.9 Safety replication: explicit ceiling effect and no identified remediation effect


In Module 2, both F_CURRENT_FULL_EAF and F_REMEDIATED_FULL_EAF produced zero unauthorized actions and zero critical unauthorized actions. VTCR was 50% in both. This created a control-arm ceiling effect for the safety endpoint: there was no comparator failure available for the remediation to eliminate. The frozen safety gates therefore passed, but the incremental remediation effect was not identified.

The model-level metrics also reveal why execution assurance must remain separate from model reasoning quality. Decision accuracy was only 15% and strict DCA only 10% in both safety arms, despite UAR=0%. External assurance can prevent unsafe execution even when the model's structured decision output remains poor.

## 6A. R3 Cross-Model Replication

### 6A.1 Frozen design and integrity

R3 (`EAF-R3-CROSS-MODEL-REPLICATION-R1`) tested whether the MAWS/EAF result survives a change in underlying local model family. Fifty deterministically selected opaque episodes from the already-frozen benchmark were evaluated under four arms: B_RAW_GOVERNANCE, L_LENGTH_MATCHED_GENERIC, M_MAWS_ONLY, and F_FULL_EAF. The existing Qwen observations for these cells were reused as an immutable anchor; Qwen was not rerun. Llama 3.1 8B, Mistral 7B, and Gemma 3 4B contributed 200 new calls each, for **600 new calls and 800 total cross-model observations**. All 600 new calls completed, and the frozen R3 result manifest is `bd9eb6d102e2539bdb6657296b64b87313c5b57d98755011c8f48124cf37a07b`.

Per-model blocks are the primary evidence. Secondary pooled statistics are reported only as a summary and are not allowed to hide a contradictory model block. R3's frozen result manifest SHA-256 is `bd9eb6d102e2539bdb6657296b64b87313c5b57d98755011c8f48124cf37a07b`; the subsequent zero-call forensic did not make model calls or mutate R3 evidence.

### 6A.2 MAWS replication across model families

| Model | B→M prompt reduction | Generic decision | MAWS decision | Δ decision | Generic VTCR | MAWS VTCR | Δ VTCR | MAWS UAR | Full-EAF UAR | Full-EAF CUA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen | 71.08% | 26.00% | 52.00% | +26 pp | 34.48% | 89.66% | +55.18 pp | 8.00% | 0.00% | 0 |
| Llama | 70.81% | 44.00% | 62.00% | +18 pp | 79.31% | 86.21% | +6.90 pp | 16.00% | 4.00% | 2 |
| Mistral | 69.63% | 42.00% | 42.00% | +0 pp | 89.66% | 89.66% | +0.00 pp | 28.00% | 4.00% | 2 |
| Gemma | 68.92% | 36.00% | 52.00% | +16 pp | 65.52% | 89.66% | +24.14 pp | 12.00% | 4.00% | 2 |

MAWS improved decision accuracy versus length-matched generic pruning in **three of four** model families and was exactly neutral in Mistral; no model reversed direction. Valid-task completion was non-worse in **four of four** model families, improving in three and remaining equal in Mistral. The preregistered cross-model support rule was therefore met.

Prompt-input reduction was strikingly stable within model family: approximately **68.92% to 71.08%** for B_RAW_GOVERNANCE→M_MAWS_ONLY. Because tokenizer and chat-template behavior differs across model families, absolute token totals are not treated as directly interchangeable across models. The combined 480,197 raw-context versus 143,776 MAWS tokens (70.06% descriptive reduction) is therefore secondary to the within-model reductions. Minimum AREPR and CAPR remained 1.0 under the frozen R3 definitions.

### 6A.3 Secondary pooled analysis

Across the 200 model-by-episode blocks, secondary pooled paired decision accuracy increased from **37% under generic pruning to 52% under MAWS**, a +15 percentage-point difference (exact McNemar p=3.59×10^-5; bootstrap 95% risk-difference CI +8 to +21.5 pp). Pooled VTCR increased from **67.24% to 88.79%** (+21.55 pp; p=5.96×10^-8).

These pooled statistics strengthen the replication signal but do not replace the model-block result: Qwen, Llama, and Gemma were positive on decision accuracy, while Mistral was neutral.

### 6A.4 Integrated assurance: risk reduction without hard-safety closure

Full EAF reduced UAR relative to MAWS-only in every model block: Qwen 8%→0%, Llama 16%→4%, Mistral 28%→4%, and Gemma 12%→4%. The secondary pooled analysis was **16%→3%**, a -13 percentage-point difference (p=2.98×10^-8; bootstrap 95% risk-difference CI -17.5 to -8.5 pp).

The stronger zero-critical-action requirement was not met across models. Full-EAF CUA counts were **Qwen=0, Llama=2, Mistral=2, Gemma=2**. Thus only one of four model blocks achieved zero critical unauthorized actions, and the frozen R3 conclusion is **INTEGRATED_ASSURANCE_SAFETY=NOT_ESTABLISHED**.

A zero-call post-hoc forensic localized all six Full-EAF critical unauthorized actions to two episode IDs repeated across Llama, Mistral, and Gemma. In every event, controlling-authority preservation was complete (2/2), pre-execution assurance classification was correct, the model decision was incorrect, the execution-permission decision was incorrect, and the same critical unauthorized action was already present in the corresponding MAWS-only arm. Administrative governance checks passed, the gate classified the evidence state as SUFFICIENT and allowed final execution, while the generic constraint evaluator recorded `NOT_EVALUATED`. The six events therefore share the conservative forensic signature `MODEL_DECISION_PLUS_EXECUTION_PERMISSION_ERROR` with `PERSISTED_FROM_MAWS_ONLY`: Full EAF failed to contain model errors that were already present under MAWS-only. Benchmark-family labels were unavailable to the forensic extractor, so no family-level concentration claim is made. This post-hoc localization does not change the failed zero-CUA safety criterion and does not establish that a single implementation patch would eliminate the failures.

The correct interpretation is therefore risk reduction rather than a safety guarantee: Full EAF consistently reduced unauthorized-action rate across the tested model families, but critical unauthorized executions remained in three model blocks.

## 7. Discussion

### 7.1 The main MAWS result is a utility-preservation result

The most important causal result is M vs L. Both arms are short, but the authority-aware working set substantially preserves decision quality and executable-task completion. This directly addresses the alternative explanation that EAF's earlier token and quality results were merely consequences of feeding the model less text.

The result also clarifies what MAWS should not be asked to do. Context selection alone cannot guarantee safe execution. M_MAWS_ONLY still produced unauthorized actions. The architecture therefore benefits from keeping context intelligence and execution assurance as separate controls rather than claiming that better context is equivalent to deterministic enforcement.

### 7.2 Safety can improve while reasoning remains weak

The contrast between UAR and strict DCA is equally important. F_FULL_EAF produced zero unauthorized actions in Module 1 even though strict DCA was only 10%. In Module 2, both safety arms again achieved zero UAR with only 15% decision accuracy. An enterprise assurance architecture should therefore measure both the model decision and the externally enforced action. Conflating them would hide the difference between a model that reasons correctly and a system that safely refuses to execute an incorrect model recommendation.

### 7.3 R2 failure strengthened the evaluation design

R2's hard-safety failure is retained because it exposed a meaningful architecture gap. The later forensic audit showed that MAWS had preserved the relevant authority evidence; the failure occurred because a model ALLOW decision was not deterministically constrained downstream. This finding led to a prospective ablation instead of a post-hoc reinterpretation. The follow-up then showed that the integrated assurance configuration can reduce UAR relative to MAWS-only, while the separate remediation replication remained inconclusive.

### 7.4 Outcome assurance remains only partially evaluated

The current experiments use symbolic execution and simplified deterministic readback. They do not evaluate eventual consistency, replica lag, asynchronous settlement, retry/stability windows, or multi-system transactions. The Authoritative Observation Contract is therefore an architectural contribution whose production-grade temporal semantics require further empirical work.

### 7.5 Cross-model replication narrows, but does not remove, the generalization boundary

R3 materially changes the generalization claim. The MAWS-vs-generic direction is no longer confined to qwen3:8b: three independent additional model families produced two positive decision-accuracy replications and one neutral result, with no negative reversal, while VTCR was non-worse in all four model blocks including the Qwen anchor. The appropriate claim is therefore bounded cross-model replication under a common synthetic benchmark, not universal LLM generalization.

The safety result is deliberately separated from this MAWS conclusion. Full EAF reduced UAR in every model block, but six critical unauthorized actions remained outside Qwen. This demonstrates why a lower average unauthorized-action rate and a zero-critical-action assurance claim are different propositions.

## 8. Threats to Validity and Limitations

**Bounded cross-model scope.** R3 replicated the core comparison across Qwen, Llama, Mistral, and Gemma under one frozen synthetic benchmark and local Ollama runtime. This removes the earlier single-model limitation but does not establish universal LLM generalization, hosted-provider generalization, scale-model generalization, or robustness to different prompt/runtime implementations.

**Synthetic benchmark.** The benchmark was deliberately structured to support exact authority, evidence, and execution labels. This improves causal interpretability but does not reproduce the messiness of live enterprise data.

**MAWS-P versus MAWS-D.** The experiment demonstrates preservation under supplied metadata. It does not prove that the system can infer authority ranks, temporal states, reliability, or mandatory evidence correctly from unstructured enterprise sources.

**Symbolic enterprise execution.** No live enterprise system was written during these studies. Outcome readback is therefore a controlled simulation of observation-contract semantics rather than a production transaction study.

**Strict decision quality remains low.** Strict DCA is low across follow-up arms, and pre-execution assurance-label accuracy is also low. The system's safety behavior should not be interpreted as high model reasoning fidelity.

**Safety replication did not expose the intended comparator failure.** Module 2 cannot establish the incremental remediation effect because both current and remediated Full EAF already achieved zero UAR/CUA.

**Multiplicity and secondary metrics.** Some large numerical differences, such as execution-permission accuracy for MAWS versus generic pruning, did not remain below 0.05 after the broad Holm correction and are therefore treated as secondary.

**Latency is descriptive.** Mean latency differs strongly by arm and over the five-hour execution window. Cache state, prompt size, runtime scheduling, and generation length can all contribute. No generalized latency claim is made.

**No monetary inference.** Prompt-token reductions are not translated into provider cost, energy, ROI, or end-to-end compute savings.

**Commercial comparison scope.** Related-work statements are based on public documentation and should not be interpreted as exhaustive implementation audits of commercial platforms.



**Cross-model hard safety remains unresolved.** Full EAF reduced UAR in all four R3 model blocks, but critical unauthorized actions remained in Llama, Mistral, and Gemma (two each). A post-hoc zero-call forensic localized all six events to two repeated episode IDs with the same model-decision-plus-execution-permission-error signature, but family labels were unavailable and the analysis cannot prove that one implementation repair would remove the failure mode. The study therefore supports cross-model risk reduction but not a zero-critical-action safety guarantee.

## 9. Claim Register for Publication

The evidence supports six primary statements.

1. MAWS preserved all available required evidence and controlling authority in the frozen follow-up benchmark while reducing aggregate model-input tokens by 72.4% relative to raw governance context.
2. At approximately the same prompt budget, MAWS outperformed generic pruning on decision accuracy and valid-task completion, supporting an authority-aware selection benefit beyond shortening alone.
3. MAWS alone did not establish a UAR improvement and should not be presented as an execution-safety mechanism.
4. Adding the integrated Full-EAF assurance configuration reduced UAR from 8% to 0% relative to MAWS-only in Module 1, while the incremental remediation effect in Module 2 remained unestablished.
5. In R3, MAWS outperformed length-matched generic pruning on decision accuracy in three of four local model families and was neutral in the fourth; VTCR was non-worse in all four, supporting bounded cross-model replication of the MAWS utility-preservation effect.
6. Full EAF reduced UAR relative to MAWS-only in all four R3 model blocks, but zero-critical-action safety was achieved in only one of four; cross-model hard safety is therefore not established.


The paper explicitly does **not** claim enterprise safety proof, universal accuracy improvement, universal cross-model generalization, a readback-only causal effect, or monetary savings from prompt-token reduction.

## 10. Conclusion

EAF reframes enterprise agent assurance as a chain of distinct obligations: determine authority, compile authoritative context, constrain execution, and verify observed outcomes. The prospective evidence supports the central MAWS proposition in a bounded but meaningful way. In the prospective follow-up, MAWS reduced aggregate model-active input by 72.40% relative to raw governance context; in R3, the corresponding within-model reductions ranged from 68.92% to 71.08%, while available required evidence and controlling authority remained fully preserved under the frozen definitions. More importantly, when compared with a generic pruning baseline at approximately the same prompt budget, MAWS retained substantially more decision accuracy and valid-task completion. This shows that the observed benefit is not explained by prompt shortening alone.

The evaluation also demonstrates why context intelligence and execution assurance should remain separate. MAWS alone did not improve UAR versus the equally short baseline, whereas the integrated Full-EAF assurance configuration reduced UAR from 8% to 0% relative to MAWS-only. At the same time, weak strict decision accuracy and an inconclusive remediation replication prevent broader claims.

The resulting research position remains deliberately bounded but is stronger after R3: **authority-aware context compilation is empirically distinguishable from generic context reduction and this utility-preservation effect reproduced across the tested local model families, while closed-loop enterprise assurance still requires controls beyond the model's own decision.** R3 also shows that consistent UAR reduction is not equivalent to zero-critical-action safety. The six observed Full-EAF critical actions collapsed to two repeated episode IDs across the three new model families and shared a model-decision-plus-execution-permission-error signature, providing a concrete containment target without converting the failed safety gate into a pass. Future work should test MAWS discovery on unstructured enterprise evidence, investigate and prospectively retest this containment failure mode, extend replication to additional model scales/providers, and evaluate observation contracts under real asynchronous enterprise state transitions.

## Appendix A. Earlier R1 pilot

An earlier 400-execution paired pilot used 200 episodes with Control and Treatment arms. The control produced 0/200 exact validations and the treatment 160/200, with no infrastructure failures. The cause of the extreme asymmetry was not established. Because output-contract symmetry and other harness concerns were corrected only in later work, the R1 result is treated as a harness-qualification anomaly and is not used to support EAF performance claims.

## Appendix B. Frozen R2 arm summary

| Arm | Prompt tokens total | UAR | Critical unauthorized actions | Decision accuracy | Execution-permission accuracy | Pre-assurance accuracy |
|---|---:|---:|---:|---:|---:|---:|
| A_NATIVE | 552,030 | 19.0% | 9 | 48.0% | 81.0% | 26.0% |
| B_GOVERNANCE | 556,290 | 19.0% | 10 | 49.0% | 81.0% | 31.0% |
| C_FULL_EAF | 167,742 | 11.5% | 10 | 63.5% | 88.5% | 70.0% |

R2's frozen status remains a failed hard-safety result because C_FULL_EAF produced ten critical unauthorized executions.

## Appendix C. Prospective follow-up arm summary

| Arm | n | Prompt tokens total | Decision accuracy | Exec-permission accuracy | VTCR | UAR | CUA |
|---|---:|---:|---:|---:|---:|---:|---:|
| B_RAW_GOVERNANCE | 100 | 238,774 | 61% | 85% | 87.27% | 11% | 4 |
| M_MAWS_ONLY | 100 | 65,901 | 54% | 86% | 87.27% | 8% | 0 |
| G_GATE_ONLY | 100 | 238,774 | 61% | 85% | 89.09% | 4% | 4 |
| L_LENGTH_MATCHED_GENERIC | 100 | 67,307 | 28% | 65% | 36.36% | 3% | 1 |
| F_FULL_EAF | 100 | 65,901 | 53% | 86% | 87.27% | 0% | 0 |
| F_CURRENT_FULL_EAF | 40 | 31,140 | 15% | 95% | 50% | 0% | 0 |
| F_REMEDIATED_FULL_EAF | 40 | 31,140 | 15% | 95% | 50% | 0% | 0 |

VTCR is defined only over cases where execution was expected; Module-1 VTCR denominator is 55.

## References (working, public documentation accessed 30 August 2026)

[1] Microsoft. “Microsoft Agent 365: The Control Plane for Agents.” https://www.microsoft.com/en-in/microsoft-agent-365

[2] Amazon Web Services. “Getting started with Policy in Amazon Bedrock AgentCore” and AgentCore Policy documentation. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-getting-started.html

[3] Google Cloud. “Set up Agent Gateway — Gemini Enterprise Agent Platform.” https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway

[4] SAP. “SAP AI Agent Hub.” https://www.sap.com/india/products/artificial-intelligence/ai-agent-hub.html

[5] ServiceNow. “Complete AI asset lifecycle — AI Control Tower.” https://www.servicenow.com/docs/r/intelligent-experiences/ai-control-tower/complete-ai-asset-lifecycle.html

[6] IBM. “Agentic Control Plane in IBM watsonx Orchestrate: One place to control every AI agent.” Published 2 July 2026. https://www.ibm.com/new/announcements/introducing-the-agentic-control-plane

## AI Assistance Disclosure

GPT-based assistance, operating under the author's guidance and authority, was used together with the author's custom AI tools and evaluation frameworks to support analysis, validation, drafting, and assessment criteria. All scientific judgments, experimental freezes, interpretations, and final claims remain the author's responsibility.


## Appendix D. Track-A Reviewer-Requested Statistical Disclosure

The complete 40-test Holm family, VTCR family, McNemar 2×2 tables, CUA diagnostics, and preservation denominators are frozen in `TRACK-A-STATISTICAL-SUPPLEMENT.md` generated from the immutable R2 follow-up ledger. This appendix is a reporting closure only and does not alter preregistered R2 or follow-up outcomes.
