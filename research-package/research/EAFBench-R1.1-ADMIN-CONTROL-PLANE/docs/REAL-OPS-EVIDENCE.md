# EAF Real Operational Evidence Layer — R1.1

## Purpose

This layer adds **observational real-runtime evidence** to EAF-RESEARCH-FOUNDATION-R1
without changing EAFBench ground truth, dataset splits, scenario families, validators,
or synthetic benchmark expectations.

The source evaluation is preserved verbatim under `real-ops/raw/`.

## Research separation

| Layer | Authority | Purpose |
|---|---|---|
| EAFBench | Deterministic benchmark truth | Controlled falsifiable evaluation |
| EAF-OPS | Observational runtime evidence | Real implementation characterization |
| Future paired cohort | Controlled empirical treatment evidence | Causal/benefit claims after floors |

EAF-OPS must never be silently promoted into benchmark ground truth.

## Normalized paired observation

Record: `EAF-OPS-000001`

- Release: **R2.0 / build R2.2.9.19**
- EIA version: **0.4.0**
- Runtime profile: **Current POC · 3.1.0-RC10.4**
- Baseline/EIA input parity: **PASS**
- Same profile/agent/system: **true / true / true**
- Baseline status: **SUCCESS**
- EIA status: **SUCCESS**
- Outcome quality: **70.0/100 vs 70.0/100**
- Baseline estimated raw context: **~9895 tokens**
- EIA estimated compact context: **~408 tokens**
- Source-reported EIA payload reduction: **95.8%**
- EIA synchronous microkernel overhead: **8450.429 ms**
- End-to-end latency: **Not measured**
- Mandatory evidence coverage: **Not measured**
- Unsupported critical claims: **Not measured**
- Reusable agents affected: **9 identified; financially unproven**

## Important measurement caveat

The token values are explicitly described by the source as transparent
**4-bytes-per-token estimates**. They are not provider-reported model-input or
billing telemetry.

The report's ~9,895 → ~408 comparison is therefore suitable as an observed
application/runtime context-boundary measurement, not as proof of equivalent
provider-input, latency, compute, or monetary-cost reduction.

## Claim gate

The source itself requires:

- 30 paired functional runs
- 100 paired latency runs
- signed benchmark evidence
- quality and evidence floors
- rollback and kill switch
- named approval

Current source state:

- functional floor met: **False**
- latency floor met: **False**
- statistical floor met: **False**
- claim permitted: **False**

Therefore this R1.1 layer remains **OBSERVATIONAL_SUPPORT**, not a causal
performance/ROI result.

## Why this matters for the paper

This record now gives the future EAF paper a real implementation case with:

1. a pinned paired workload contract;
2. evidence and output hashes;
3. explicit enterprise/agent/EIA/LLM authority roles;
4. a deterministic evidence funnel;
5. a measured coordination overhead;
6. a context-boundary measurement;
7. an explicit claim-governance gate;
8. preserved missing measurements and non-activated controls.

That is stronger than a screenshot or architecture diagram while still respecting
the evidence boundary.
