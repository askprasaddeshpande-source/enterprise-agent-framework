# Decisions

## D001 — EAF positioning
EAF is positioned as an **Enterprise Agent Administration & Runtime Control Plane**,
not merely as another agent orchestration framework.

## D002 — Evidence separation
Synthetic benchmark truth and real operational evidence remain separate.

## D003 — Ground truth
Benchmark ground truth is deterministic and model-independent.

## D004 — Differential-context design
Dataset breadth is measured through material context/admin-state variation, not
prompt-count inflation.

## D005 — No post-hoc repair
Frozen expected outcomes must not be changed merely because an EAF treatment
disagrees with them.

## D006 — Real EIA data
Real EIA reports are observational support. They are not causal treatment evidence
until the source-defined paired sample floors and approvals are satisfied.

## D007 — Claim discipline
Application-level token/context estimates are not provider-metered model-input,
latency, cost, or ROI proof.

## D008 — SAP role
SAP remains the deepest reference implementation, while EAF contracts remain
vendor-neutral.

## D009 — Signing
All executable research scripts must be digitally signed. Release manifests must
be cryptographically signed before a package is represented as signed/frozen.
