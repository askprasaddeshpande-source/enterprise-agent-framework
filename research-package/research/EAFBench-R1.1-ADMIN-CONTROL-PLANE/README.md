# EAF-RESEARCH-FOUNDATION-R1

Repo-ready research foundation for the **Enterprise Agent Framework (EAF)** and
its evaluation benchmark **EAFBench**.

## What is included

1. EAF-R2A frozen-contract candidate
2. Machine-readable ontology and invariants
3. JSON Schemas
4. Five enterprise domain templates
5. Twenty-four scenario families
6. Deterministic context-differential generator
7. Deterministic validator
8. Dataset split policy
9. Metrics including GTS, UAR, ARA, CER, PCR, CSA, and CIR
10. A/B experiment packet harness
11. 2,400-episode benchmark snapshot
12. Golden dataset, held-out set, falsification set
13. Hash manifest and detached Ed25519 signatures for executable Python scripts
14. Tests and acceptance report

## Key research boundary

`MODEL_EXPERIMENTS_EXECUTED=0`

This package builds the benchmark foundation only. It does not claim that an
EAF treatment is superior, safer, or empirically validated.

## Dataset design

The snapshot contains:

- 100 canonical missions
- 5 domains
- 20 canonical missions per domain
- 24 differential context variants per canonical mission
- 2,400 executable episodes

The same mission is re-issued under different evidence, authority, temporal,
approval, capability, policy, provenance, and outcome conditions.

This allows measurement of:

- **CSA** — Context Sensitivity Accuracy: does the decision change when
  governing context changes?
- **CIR** — Context Invariance Rate: does the decision remain stable when
  irrelevant, stale-but-noncontrolling, duplicate, or malicious context should
  not alter the outcome?

## Run locally

From repository root:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m eafbench.build_dataset --missions-per-domain 20
python -m eafbench.characterize dataset/eafbench-v0.1.jsonl --out evidence/dataset-characterization.json
python -m eafbench.verify_signatures
```

Set:

```bash
export PYTHONPATH=src
```

or install the package in editable mode after adding your preferred packaging
metadata.

## Signing note

All executable `.py` files in this release have detached **Ed25519 artifact
signatures** under `signatures/`.

These signatures prove integrity relative to the included release public key.
They are **not** an identity-attested replacement for your approved Windows
Authenticode/code-signing certificate. Before a production or organizational
release, re-sign under your approved certificate/key-management process.

The private signing key used to create this bundle is not included.

## R1.1 Real Operational Evidence Layer

This bundle now includes `real-ops/`, containing a preserved EIA Trust & Value
Evaluation and normalized EAF-OPS observational record.

Important: EAF-OPS is **observational support** and does not modify EAFBench
ground truth or establish causal EAF superiority. See `docs/REAL-OPS-EVIDENCE.md`.


## R1.1 Administration & Control Plane Extension

`admin-control-plane/` adds a dedicated benchmark for EAF's proposed role as an
enterprise administration and runtime-control layer.

Current extension:
- 2000 deterministic admin/control episodes
- 100 canonical admin missions
- 100 differential sets
- 20 administrative scenario families
- 5 enterprise domains
- zero evaluated-model executions

The original `dataset/eafbench-v0.1.jsonl` and `real-ops/raw/` evidence are
preserved unchanged.
