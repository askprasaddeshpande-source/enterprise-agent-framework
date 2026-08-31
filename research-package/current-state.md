# Current State

## Project
Enterprise Agent Framework (EAF) Whitepaper + EAFBench research program.

## Current objective
Freeze a defensible benchmark and evidence program before running treatment
experiments, then evaluate whether a dedicated enterprise agent administration
and runtime-control plane improves governed task behavior.

## Authoritative state
`research/EAFBench-R1.1-ADMIN-CONTROL-PLANE/`

## Research corpus

### EAFBench v0.1
- 100 canonical missions
- 24 differential context variants per mission
- 2,400 episodes
- 5 domains
- evidence/authority/temporal/policy/capability/readback scenarios

### EAFBench R1.1 Admin Control Plane
- 100 canonical administrative missions
- 20 administrative differential variants per mission
- 2,000 episodes
- 5 domains
- registration/tenant/lifecycle/grants/delegation/approval/revocation/model/tool/
  kill-switch/audit/readback scenarios

### Combined controlled corpus
**4,400 deterministic episodes**

### Real operational evidence
One normalized paired EIA evaluation is preserved as **observational support**:
- input parity recorded PASS;
- direct baseline and EIA run both SUCCESS;
- outcome quality 70/100 vs 70/100;
- application-level context estimate ~9,895 vs ~408 tokens;
- EIA synchronous overhead 8,450.429 ms;
- end-to-end latency not measured;
- claim floors not met;
- causal benefit claim not established.

## Current blockers
1. Human semantic review of benchmark expectations and administrative decisions.
2. Freeze of treatment acceptance thresholds before model execution.
3. Real paired cohort evidence remains below required functional/latency floors.
4. No causal claims about EAF quality, cost, latency, ROI, or safety are permitted yet.

## Next action
Review and freeze the 44 differential scenario families and experiment contract.
Then run a bounded Control A vs Treatment B pilot on a development-only subset.
