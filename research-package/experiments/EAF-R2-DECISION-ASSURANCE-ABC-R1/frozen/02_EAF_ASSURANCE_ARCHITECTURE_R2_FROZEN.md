# EAF Assurance Architecture R2 — Frozen Pre-Inference Contract

## Pipeline

```text
Mission
  ↓
Mission Normalizer
  ↓
Candidate Evidence Universe
(SAP / API / MCP / RAG / Vector / Memory / Policies / Tools)
  ↓
Identity / Tenant / Lifecycle Gate
  ↓
Authority + Temporal + Reliability Resolver
  ↓
Evidence Sufficiency / Conflict Gate
  ↓
Minimum Authoritative Working Set (MAWS)
  ├──────────────→ Full immutable audit plane
  ↓
Compact model-active wire plane
  ↓
LLM proposal
  ↓
Deterministic Policy / Approval / Runtime Gate
  ↓
Symbolic or real enterprise execution
  ↓
Independent authoritative readback
  ↓
Validated outcome / mismatch / unverified
```

## Frozen R2 invariants

R2-I01 Identity is not inferred by the model.  
R2-I02 Capability is not authority.  
R2-I03 Permission is not evidence sufficiency.  
R2-I04 Retrieval relevance is not enterprise authority.  
R2-I05 Current controlling evidence normally governs current-state decisions.  
R2-I06 Authority rank alone is insufficient when strongest evidence reliability is materially weak and strongly validated contradictory evidence exists.  
R2-I07 Equal-authority contradiction is not silently merged.  
R2-I08 Unknown is not inferred.  
R2-I09 Mandatory evidence cannot be dropped for token reduction.  
R2-I10 Controlling authority cannot be dropped for token reduction.  
R2-I11 Required unresolved conflicts cannot be hidden for token reduction.  
R2-I12 Audit evidence and model-active evidence are separate planes.  
R2-I13 Model-context exclusion does not delete durable evidence.  
R2-I14 Every admitted fact has provenance.  
R2-I15 Every excluded candidate has a reason.  
R2-I16 Unneeded tools/skills are context and may be withheld.  
R2-I17 Policy/approval enforcement remains outside the model.  
R2-I18 Execution response is not validated success.  
R2-I19 Consequential success requires authoritative readback when the mission contract requires it.  
R2-I20 Readback mismatch is a first-class outcome.  
R2-I21 Readback authority/system/tenant must match the intended target.  
R2-I22 Assurance state is evidence-derived, not model self-confidence.  
R2-I23 Selective bypass is deterministic and cannot bypass a high-risk/readback-required mission.  
R2-I24 If hard-required evidence exceeds context budget, fail explicitly rather than silently dropping it.  
R2-I25 Scientific metrics remain separated; no composite score is manufactured post hoc.
