# Next Executable Prompt

## RUN_ID
EAFBENCH_R1_1_ADMIN_CONTROL_PLANE_REVIEW_AND_FREEZE_R1

## Role
Act as an independent senior AI systems researcher and enterprise architecture reviewer.

## Authoritative root
`research/EAFBench-R1.1-ADMIN-CONTROL-PLANE/`

## Objective
Perform a bounded semantic review and freeze assessment of the combined EAFBench
research corpus before any evaluated LLM experiment is allowed.

## Scope
Review:
1. 24 original EAFBench evidence/authority/context scenario families.
2. 20 Administration & Control Plane scenario families.
3. Expected decisions, forbidden actions and validator predicates.
4. Held-out/adversarial/falsification split integrity.
5. Metric definitions and acceptance thresholds.
6. Claim boundaries and real-ops evidence separation.

## Constraints
- Do not change benchmark outcomes merely to make EAF easier to pass.
- Do not execute an evaluated LLM treatment.
- Do not expose held-out/falsification truth to implementation code.
- Preserve all existing datasets and hashes.
- Any proposed semantic correction must be reported as a versioned benchmark defect,
  with original evidence retained.
- Do not modify raw real-ops evidence.
- All executable scripts created or modified must be digitally signed.

## Required output
Produce:
- REVIEW-REPORT.md
- SEMANTIC-ISSUES.json
- FREEZE-DECISION.json
- THRESHOLDS-FROZEN.json
- updated signed release manifest only if changes are explicitly approved

## Acceptance
The review may conclude PASS, PASS_WITH_VERSIONED_CORRECTIONS, or HOLD.
Model A/B execution remains prohibited until FREEZE-DECISION=PASS.
