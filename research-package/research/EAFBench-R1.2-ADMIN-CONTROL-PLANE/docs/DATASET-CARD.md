# EAFBench v0.1 Dataset Card

## Purpose

EAFBench evaluates authority-aware enterprise-agent behavior. It is not an
initial training dataset.

## Ground truth

Ground truth is programmatically generated from canonical enterprise state and
policy rules. The evaluated model has zero authority to define expected labels.

## Domains

- Procurement / Finance
- Enterprise IT Operations
- Software Engineering / Deployment
- Customer Operations
- SAP / ERP

## Differential-context structure

Each canonical mission is represented as a Context Differential Set (CDS) with
24 variants. Variants alter material or non-material context while preserving
the mission identity.

This supports both:
- decision sensitivity to material governance changes; and
- decision invariance to non-controlling context.

## Known limitations

- Domain simulators are synthetic reference environments.
- Current decisions are rule-derived; they are not a substitute for real
  enterprise authorization engines.
- No model A/B experiment is included in R1.
- The dataset is balanced by construction across scenario families and should
  not be interpreted as a natural production frequency distribution.
- The included Ed25519 release signature is an artifact-integrity signature,
  not an organization-identity certificate.
