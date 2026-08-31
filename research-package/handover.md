# EAF Handover

## Project
Enterprise Agent Framework (EAF)

## Current Objective
Complete semantic review and freeze of the 4,400-case research corpus, then run
the first bounded Control A vs Treatment B experiment.

## Authoritative Root
`research/EAFBench-R1.1-ADMIN-CONTROL-PLANE/`

## What is complete
- Research contract and novelty boundary candidate.
- Deterministic benchmark infrastructure.
- 2,400 authority/evidence/context episodes.
- Real EIA operational evidence ingestion.
- 2,000 administration/runtime-control episodes.
- Deterministic validators.
- Differential metrics.
- Held-out/adversarial/falsification splits.
- Signed executable scripts and signed release manifest inside the authoritative root.
- Consolidated top-level evidence and continuity docs.

## Verified facts
- Existing original EAFBench dataset remained unchanged when the admin extension was built.
- Raw real EIA operational evidence remained unchanged.
- Latest benchmark extension tests passed.
- No evaluated-model experiment has been executed by the research foundation.
- Real source claim floors are not met.

## Current blocker
The next valid action is **human semantic review/freeze**, not model evaluation.

## Do not do
- Do not tune EAF against held-out/falsification labels.
- Do not rewrite benchmark truth after seeing treatment performance.
- Do not claim provider-token, latency, cost, ROI or safety improvement from current real-ops evidence.
- Do not mix EAF-OPS observational records into deterministic benchmark ground truth.

## Next executable work
Follow `next-executable-prompt.md`.
