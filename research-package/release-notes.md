# Release Notes

## EAF-CONSOLIDATED-RESEARCH-PACKAGE-R1 — 2026-08-29

### Consolidated
- EAF-R2A research contract
- 24 frozen evidence/authority invariants
- EAFBench v0.1 deterministic generator and 2,400-episode corpus
- EAF operational evidence layer from real EIA reports
- Normalized EAF-OPS observation
- EAF Administration & Control Plane contract
- 20 admin-plane invariants
- 2,000 admin/control-plane episodes
- Held-out, adversarial and falsification datasets
- Deterministic validators and metrics
- Release/signature verification infrastructure
- Source EIA UI screenshots
- Handover/current-state/architecture/decisions/backlog docs

### Current total
- Controlled benchmark episodes: 4,400
- Real normalized observational records: 1
- Evaluated-model experiments: 0

### No new scientific claim
This consolidation does not convert benchmark self-consistency or one operational
pair into evidence of EAF superiority.

## R1.2 Versioned Benchmark Correction
- C001_F05_F06_AUTHORITY_DISTINCTION: F05 now represents authorized requester + absent execution authority; F06 represents requester authority absent.
- C004_CONSEQUENTIAL_READBACK_NEXT_ACTION: All normally allowed consequential paths now use EXECUTE_THEN_VALIDATE; post-execution outcome determines validated success.
- C002_A05_CURRENT_POLICY_LABEL: A05 uses DENY_CURRENT_POLICY.
- C003_A15_RETIRED_AGENT_LABEL: A15 uses DENY_RETIRED_AGENT.
- R1.1 preserved. No evaluated-model/treatment result was used.
