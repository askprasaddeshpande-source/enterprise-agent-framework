# EAF Consolidated Research Package R1

This is the consolidated handover package for the **Enterprise Agent Framework
(EAF)** research program as of 2026-08-29.

## Authoritative project root

`research/EAFBench-R1.1-ADMIN-CONTROL-PLANE/`

Do not reconstruct the project from older intermediate packages. The authoritative
root already contains:

1. the original EAF research contract;
2. EAFBench v0.1 — 2,400 evidence/authority/context episodes;
3. real EIA operational evidence and normalized observational record;
4. EAFBench R1.1 Administration & Control Plane — 2,000 additional episodes;
5. deterministic validators, tests, evidence manifests and release signatures.

## Current scientific state

**Synthetic/controlled benchmark corpus:** 4,400 episodes  
**Real operational normalized observations:** 1 paired observation  
**Evaluated LLM experiments:** 0  
**Overall status:** FREEZE CANDIDATE / READY FOR HUMAN SEMANTIC REVIEW

The 4,400 benchmark episodes are not empirical EAF performance results. Oracle
scores validate benchmark self-consistency only.

## Central architecture proposition

EAF is being evaluated as an **enterprise administration and runtime-control
plane between AI/LLM agents and authoritative enterprise systems**.

It does not replace:
- model intelligence;
- enterprise system-of-record truth;
- native enterprise authorization;
- human accountability.

## Next gate

`EAFBench-R1.1-ADMIN-CONTROL-PLANE-REVIEW-AND-FREEZE`

Only after semantic review/freeze should the controlled experiment begin:

**Control A:** same agent/workload without EAF administration/control treatment  
**Treatment B:** same agent/workload with EAF administration/control treatment
