# EAFBench Decision Assurance R2

## Size

20 scenario families × 10 variants = **200 episodes**.

Split inside each family:
- V01–V06: DEVELOPMENT (120 total)
- V07–V08: HELDOUT (40 total)
- V09–V10: ADVERSARIAL (40 total)

All are frozen before model inference.

## Families

D01 STALE_EVIDENCE  
D02 SUPERSEDED_AUTHORITY  
D03 DUPLICATE_EVIDENCE  
D04 IRRELEVANT_ENTERPRISE_HISTORY  
D05 LOW_AUTHORITY_DISTRACTOR  
D06 MANDATORY_EVIDENCE_MISSING  
D07 EQUAL_AUTHORITY_CONFLICT  
D08 FALSE_HIGH_AUTHORITY  
D09 TOOL_SURFACE_NOISE  
D10 POLICY_CONTEXT_NOISE  
D11 HISTORICAL_VS_CURRENT_STATE  
D12 UNKNOWN_FIELD_PRESSURE  
D13 UNSUPPORTED_CRITICAL_CLAIM  
D14 READBACK_SUCCESS  
D15 READBACK_FAILURE  
D16 OUTCOME_MISMATCH  
D17 PARTIAL_EXECUTION  
D18 SELECTIVE_BYPASS  
D19 GOVERNANCE_NOT_REQUIRED  
D20 HIGH_RISK_ASSURANCE_REQUIRED

## Model leakage prohibition

The model receives:
- episode id;
- mission;
- raw or compiled observation depending on arm;
- arm-specific control envelope where applicable.

The model never receives:
- family id;
- split;
- canonical truth;
- expected output;
- validator;
- hidden readback truth.

## LLM judge

Prohibited. Evaluation is deterministic.
