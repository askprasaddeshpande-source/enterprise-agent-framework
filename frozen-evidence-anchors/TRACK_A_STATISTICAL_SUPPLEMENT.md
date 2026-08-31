# EAF Track A — Zero-Call Statistical Reporting Supplement

Analysis: `EAF-TRACK-A-REVIEWER-ADJUDICATION-R1`

## Integrity

- Frozen R2 follow-up observations used: **580**
- New model calls: **0**
- Bootstrap: percentile paired risk-difference interval, **5,000 resamples**, RNG seed **20260830**.

## Dual token reporting

- B→M aggregate total-token reduction: **72.40%**.
- B→M paired mean episode reduction: **59.53%**.
- B→M paired median episode reduction: **71.76%**.
- These are different estimands: aggregate reduction weights episodes by raw token volume; paired mean weights episodes equally.

## F vs G — previously named but unreported ablation

- G decision accuracy: 61.00%; F: 53.00%.
- G VTCR: 89.09%; F: 87.27%.
- G UAR: 4.00%; F: 0.00%.
- G CUA: 4; F CUA: 0.

The paired rows below provide the exact inferential results. F-vs-G must be interpreted as the incremental MAWS-plus-associated-full-configuration contrast within the frozen design, not as a universal component effect.

## Complete paired binary family used by the scientific-closure global Holm correction

| Comparison | Metric | rate A | rate B | RD B-A | n00 | b01 | b10 | n11 | raw p | Holm p |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B_vs_M | decision_accuracy | 61.00% | 54.00% | -7.00% | 33 | 6 | 13 | 48 | 0.16706848 | 1 |
| B_vs_M | execution_permission_accuracy | 85.00% | 86.00% | 1.00% | 10 | 5 | 4 | 81 | 1 | 1 |
| B_vs_M | next_action_accuracy | 46.00% | 28.00% | -18.00% | 53 | 1 | 19 | 27 | 4.0054321e-05 | 0.0015621185 |
| B_vs_M | pre_assurance_accuracy | 24.00% | 22.00% | -2.00% | 73 | 3 | 5 | 19 | 0.7265625 | 1 |
| B_vs_M | strict_decision_contract_accuracy | 9.00% | 10.00% | 1.00% | 90 | 1 | 0 | 9 | 1 | 1 |
| B_vs_M | mission_evidence_sufficiency_accuracy | 95.00% | 95.00% | 0.00% | 5 | 0 | 0 | 95 | 1 | 1 |
| B_vs_M | unauthorized_action | 11.00% | 8.00% | -3.00% | 88 | 1 | 4 | 7 | 0.375 | 1 |
| B_vs_M | critical_unauthorized_action | 4.00% | 0.00% | -4.00% | 96 | 0 | 4 | 0 | 0.125 | 1 |
| B_vs_G | decision_accuracy | 61.00% | 61.00% | 0.00% | 38 | 1 | 1 | 60 | 1 | 1 |
| B_vs_G | execution_permission_accuracy | 85.00% | 85.00% | 0.00% | 14 | 1 | 1 | 84 | 1 | 1 |
| B_vs_G | next_action_accuracy | 46.00% | 50.00% | 4.00% | 49 | 5 | 1 | 45 | 0.21875 | 1 |
| B_vs_G | pre_assurance_accuracy | 24.00% | 25.00% | 1.00% | 75 | 1 | 0 | 24 | 1 | 1 |
| B_vs_G | strict_decision_contract_accuracy | 9.00% | 9.00% | 0.00% | 91 | 0 | 0 | 9 | 1 | 1 |
| B_vs_G | mission_evidence_sufficiency_accuracy | 95.00% | 95.00% | 0.00% | 5 | 0 | 0 | 95 | 1 | 1 |
| B_vs_G | unauthorized_action | 11.00% | 4.00% | -7.00% | 89 | 0 | 7 | 4 | 0.015625 | 0.546875 |
| B_vs_G | critical_unauthorized_action | 4.00% | 4.00% | 0.00% | 96 | 0 | 0 | 4 | 1 | 1 |
| L_vs_M | decision_accuracy | 28.00% | 54.00% | 26.00% | 33 | 39 | 13 | 15 | 0.00040954145 | 0.015562575 |
| L_vs_M | execution_permission_accuracy | 65.00% | 86.00% | 21.00% | 3 | 32 | 11 | 54 | 0.001913961 | 0.070816557 |
| L_vs_M | next_action_accuracy | 24.00% | 28.00% | 4.00% | 61 | 15 | 11 | 13 | 0.55719709 | 1 |
| L_vs_M | pre_assurance_accuracy | 22.00% | 22.00% | 0.00% | 68 | 10 | 10 | 12 | 1 | 1 |
| L_vs_M | strict_decision_contract_accuracy | 6.00% | 10.00% | 4.00% | 85 | 9 | 5 | 1 | 0.4239502 | 1 |
| L_vs_M | mission_evidence_sufficiency_accuracy | 95.00% | 95.00% | 0.00% | 5 | 0 | 0 | 95 | 1 | 1 |
| L_vs_M | unauthorized_action | 3.00% | 8.00% | 5.00% | 89 | 8 | 3 | 0 | 0.2265625 | 1 |
| L_vs_M | critical_unauthorized_action | 1.00% | 0.00% | -1.00% | 99 | 0 | 1 | 0 | 1 | 1 |
| M_vs_F | decision_accuracy | 54.00% | 53.00% | -1.00% | 46 | 0 | 1 | 53 | 1 | 1 |
| M_vs_F | execution_permission_accuracy | 86.00% | 86.00% | 0.00% | 13 | 1 | 1 | 85 | 1 | 1 |
| M_vs_F | next_action_accuracy | 28.00% | 30.00% | 2.00% | 69 | 3 | 1 | 27 | 0.625 | 1 |
| M_vs_F | pre_assurance_accuracy | 22.00% | 22.00% | 0.00% | 78 | 0 | 0 | 22 | 1 | 1 |
| M_vs_F | strict_decision_contract_accuracy | 10.00% | 10.00% | 0.00% | 90 | 0 | 0 | 10 | 1 | 1 |
| M_vs_F | mission_evidence_sufficiency_accuracy | 95.00% | 95.00% | 0.00% | 5 | 0 | 0 | 95 | 1 | 1 |
| M_vs_F | unauthorized_action | 8.00% | 0.00% | -8.00% | 92 | 0 | 8 | 0 | 0.0078125 | 0.28125 |
| M_vs_F | critical_unauthorized_action | 0.00% | 0.00% | 0.00% | 100 | 0 | 0 | 0 | 1 | 1 |
| G_vs_F | decision_accuracy | 61.00% | 53.00% | -8.00% | 33 | 6 | 14 | 47 | 0.1153183 | 1 |
| G_vs_F | execution_permission_accuracy | 85.00% | 86.00% | 1.00% | 9 | 6 | 5 | 80 | 1 | 1 |
| G_vs_F | next_action_accuracy | 50.00% | 30.00% | -20.00% | 48 | 2 | 22 | 28 | 3.5881996e-05 | 0.0014352798 |
| G_vs_F | pre_assurance_accuracy | 25.00% | 22.00% | -3.00% | 72 | 3 | 6 | 19 | 0.5078125 | 1 |
| G_vs_F | strict_decision_contract_accuracy | 9.00% | 10.00% | 1.00% | 90 | 1 | 0 | 9 | 1 | 1 |
| G_vs_F | mission_evidence_sufficiency_accuracy | 95.00% | 95.00% | 0.00% | 5 | 0 | 0 | 95 | 1 | 1 |
| G_vs_F | unauthorized_action | 4.00% | 0.00% | -4.00% | 96 | 0 | 4 | 0 | 0.125 | 1 |
| G_vs_F | critical_unauthorized_action | 4.00% | 0.00% | -4.00% | 96 | 0 | 4 | 0 | 0.125 | 1 |

The global family contains **40 tests**: 5 preregistered arm pairs × 8 binary metrics.

## VTCR paired family

| Comparison | Metric | rate A | rate B | RD B-A | n00 | b01 | b10 | n11 | raw p | Holm p |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B_vs_M | valid_task_completion_rate | 87.27% | 87.27% | 0.00% | 6 | 1 | 1 | 47 | 1 | 1 |
| B_vs_G | valid_task_completion_rate | 87.27% | 89.09% | 1.82% | 6 | 1 | 0 | 48 | 1 | 1 |
| L_vs_M | valid_task_completion_rate | 36.36% | 87.27% | 50.91% | 6 | 29 | 1 | 19 | 5.7742e-08 | 2.8871e-07 |
| M_vs_F | valid_task_completion_rate | 87.27% | 87.27% | 0.00% | 6 | 1 | 1 | 47 | 1 | 1 |
| G_vs_F | valid_task_completion_rate | 89.09% | 87.27% | -1.82% | 5 | 1 | 2 | 47 | 1 | 1 |

The VTCR Holm family contains **5 tests**, one for each primary arm pair.

## Critical Unauthorized Action diagnostic family

| Comparison | Metric | rate A | rate B | RD B-A | n00 | b01 | b10 | n11 | raw p | Holm p |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B_vs_M | critical_unauthorized_action | 4.00% | 0.00% | -4.00% | 96 | 0 | 4 | 0 | 0.125 | 0.625 |
| B_vs_G | critical_unauthorized_action | 4.00% | 4.00% | 0.00% | 96 | 0 | 0 | 4 | 1 | 1 |
| L_vs_M | critical_unauthorized_action | 1.00% | 0.00% | -1.00% | 99 | 0 | 1 | 0 | 1 | 1 |
| M_vs_F | critical_unauthorized_action | 0.00% | 0.00% | 0.00% | 100 | 0 | 0 | 0 | 1 | 1 |
| G_vs_F | critical_unauthorized_action | 4.00% | 0.00% | -4.00% | 96 | 0 | 4 | 0 | 0.125 | 0.625 |

**Boundary:** CUA reviewer analysis is post-hoc diagnostic reporting requested after manuscript review. It does not retroactively become a preregistered confirmatory family.

## MAWS preservation denominators

- Preflight episodes checked: **140**.
- AREPR: **202/202** available-required evidence items preserved.
- CAPR: **202/202** controlling-authority items preserved.
- Minimum per-episode AREPR: **1.0**.
- Minimum per-episode CAPR: **1.0**.

## Holm-family reconstruction

### Global 40-test family

| Rank | Test | Raw p | Multiplier | Holm adjusted p |
|---:|---|---:|---:|---:|
| 1 | G_vs_F:next_action_accuracy | 3.5881996e-05 | 40 | 0.0014352798 |
| 2 | B_vs_M:next_action_accuracy | 4.0054321e-05 | 39 | 0.0015621185 |
| 3 | L_vs_M:decision_accuracy | 0.00040954145 | 38 | 0.015562575 |
| 4 | L_vs_M:execution_permission_accuracy | 0.001913961 | 37 | 0.070816557 |
| 5 | M_vs_F:unauthorized_action | 0.0078125 | 36 | 0.28125 |
| 6 | B_vs_G:unauthorized_action | 0.015625 | 35 | 0.546875 |
| 7 | G_vs_F:decision_accuracy | 0.1153183 | 34 | 1 |
| 8 | B_vs_M:critical_unauthorized_action | 0.125 | 33 | 1 |
| 9 | G_vs_F:critical_unauthorized_action | 0.125 | 32 | 1 |
| 10 | G_vs_F:unauthorized_action | 0.125 | 31 | 1 |
| 11 | B_vs_M:decision_accuracy | 0.16706848 | 30 | 1 |
| 12 | B_vs_G:next_action_accuracy | 0.21875 | 29 | 1 |
| 13 | L_vs_M:unauthorized_action | 0.2265625 | 28 | 1 |
| 14 | B_vs_M:unauthorized_action | 0.375 | 27 | 1 |
| 15 | L_vs_M:strict_decision_contract_accuracy | 0.4239502 | 26 | 1 |
| 16 | G_vs_F:pre_assurance_accuracy | 0.5078125 | 25 | 1 |
| 17 | L_vs_M:next_action_accuracy | 0.55719709 | 24 | 1 |
| 18 | M_vs_F:next_action_accuracy | 0.625 | 23 | 1 |
| 19 | B_vs_M:pre_assurance_accuracy | 0.7265625 | 22 | 1 |
| 20 | B_vs_G:critical_unauthorized_action | 1 | 21 | 1 |
| 21 | B_vs_G:decision_accuracy | 1 | 20 | 1 |
| 22 | B_vs_G:execution_permission_accuracy | 1 | 19 | 1 |
| 23 | B_vs_G:mission_evidence_sufficiency_accuracy | 1 | 18 | 1 |
| 24 | B_vs_G:pre_assurance_accuracy | 1 | 17 | 1 |
| 25 | B_vs_G:strict_decision_contract_accuracy | 1 | 16 | 1 |
| 26 | B_vs_M:execution_permission_accuracy | 1 | 15 | 1 |
| 27 | B_vs_M:mission_evidence_sufficiency_accuracy | 1 | 14 | 1 |
| 28 | B_vs_M:strict_decision_contract_accuracy | 1 | 13 | 1 |
| 29 | G_vs_F:execution_permission_accuracy | 1 | 12 | 1 |
| 30 | G_vs_F:mission_evidence_sufficiency_accuracy | 1 | 11 | 1 |
| 31 | G_vs_F:strict_decision_contract_accuracy | 1 | 10 | 1 |
| 32 | L_vs_M:critical_unauthorized_action | 1 | 9 | 1 |
| 33 | L_vs_M:mission_evidence_sufficiency_accuracy | 1 | 8 | 1 |
| 34 | L_vs_M:pre_assurance_accuracy | 1 | 7 | 1 |
| 35 | M_vs_F:critical_unauthorized_action | 1 | 6 | 1 |
| 36 | M_vs_F:decision_accuracy | 1 | 5 | 1 |
| 37 | M_vs_F:execution_permission_accuracy | 1 | 4 | 1 |
| 38 | M_vs_F:mission_evidence_sufficiency_accuracy | 1 | 3 | 1 |
| 39 | M_vs_F:pre_assurance_accuracy | 1 | 2 | 1 |
| 40 | M_vs_F:strict_decision_contract_accuracy | 1 | 1 | 1 |

### VTCR 5-test family

| Rank | Test | Raw p | Multiplier | Holm adjusted p |
|---:|---|---:|---:|---:|
| 1 | L_vs_M | 5.7742e-08 | 5 | 2.8871e-07 |
| 2 | B_vs_G | 1 | 4 | 1 |
| 3 | B_vs_M | 1 | 3 | 1 |
| 4 | G_vs_F | 1 | 2 | 1 |
| 5 | M_vs_F | 1 | 1 | 1 |
