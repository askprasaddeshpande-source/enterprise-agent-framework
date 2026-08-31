# Research Methodology

The foundation intentionally follows staged empirical discipline:

- **R2A:** freeze contract, ontology, invariants, schemas, metrics, and split rules.
- **R2B:** deterministic generator and reproducibility checks.
- **R2C:** deterministic framework logic evaluation before model involvement.
- **R2D:** controlled model A/B with the same mission, evidence, tools, and model.
- **R2E:** held-out, adversarial, and falsification evaluation.
- **R2F:** sanitized enterprise reference validation, including SAP as a deep case.

No R2D-R2F result exists in this release.

## No post-hoc repair

Once a benchmark release is frozen, expected outcomes and validators must not
be changed merely because an EAF implementation disagrees with them. Genuine
benchmark defects require a new dataset version and preserved historical result.
