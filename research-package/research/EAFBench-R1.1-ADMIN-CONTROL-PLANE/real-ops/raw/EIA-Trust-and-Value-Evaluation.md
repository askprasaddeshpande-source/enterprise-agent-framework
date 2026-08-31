# EIA Trust & Value Evaluation

Generated 2026-08-29T07:20:52.591Z

## Selective invocation

```
{
  "recommended_path": "BALANCED",
  "recommended_mode": "Balanced",
  "yes_count": 3,
  "signal_count": 4,
  "signals": [
    {
      "id": "MULTI_SOURCE",
      "label": "Multiple SAP or knowledge sources required",
      "yes": true,
      "evidence": "Route:c6f14c11, SAP"
    },
    {
      "id": "EVIDENCE_UNCERTAINTY",
      "label": "Evidence may be missing, stale or contradictory",
      "yes": true,
      "evidence": "Evidence gap, freshness or conflict signal detected"
    },
    {
      "id": "DECISION_RISK",
      "label": "Decision has operational, financial or compliance risk",
      "yes": false,
      "evidence": "Low-risk context"
    },
    {
      "id": "PORTFOLIO_REUSE",
      "label": "Capability or policy can be reused across agents",
      "yes": true,
      "evidence": "Admitted reusable skill/policy contract"
    }
  ],
  "score": 3,
  "scoring_model": "Four binary signals; no weights",
  "reasons": [
    "Multiple SAP or knowledge sources required",
    "Evidence may be missing, stale or contradictory",
    "Capability or policy can be reused across agents"
  ],
  "statement": "Use bounded evidence validation and context preparation.",
  "advisory_only": true
}
```

## Trust case

```
{
  "enterprise_truth_owner": "SAP and registered enterprise sources",
  "agent_role": "Orchestrates the task and owns the final response",
  "eia_role": "Validates, deduplicates, correlates and traces evidence before model reasoning",
  "llm_role": "Interpretation, explanation and decision support only",
  "deterministic_outside_llm": [
    "identity and tenant validation",
    "skill and MCP admission",
    "source authority",
    "evidence integrity",
    "mandatory evidence floor",
    "route and policy gates"
  ],
  "proof": {
    "input_parity": "PASS",
    "evidence_trace_id": "9059c404-2fb7-4c3a-8ae8-9e995615b977",
    "alignment_id": "rv-217c1ba00e46d58e",
    "source_routes": [
      {
        "service_id": "custom_st22_agent_service",
        "entity_set": "DumpHeader",
        "system_id": "PAL"
      }
    ],
    "tools": [],
    "coverage": {
      "count": 4,
      "authoritative": 2,
      "supporting": 2
    },
    "payload_reduction_pct": 95.8,
    "overhead_ms": 8450.429,
    "fallback_reason": ""
  }
}
```

## Evidence funnel

```
[
  {
    "stage": "Raw enterprise signals",
    "owner": "SAP / MCP / RAG / Vector",
    "records": 100,
    "bytes": 38899
  },
  {
    "stage": "Validated and authoritative",
    "owner": "EIA evidence contract",
    "records": 100,
    "coverage": {
      "count": 4,
      "authoritative": 2,
      "supporting": 2
    }
  },
  {
    "stage": "Deduplicated and correlated",
    "owner": "Deterministic evidence layer",
    "duplicates_removed": 0,
    "conflicts": 0
  },
  {
    "stage": "Compact model context",
    "owner": "Context boundary",
    "bytes": 1629,
    "estimated_tokens": 408
  },
  {
    "stage": "Interpretation and explanation",
    "owner": "LLM / Agent Hub",
    "final_owner": "Agent Hub"
  }
]
```

## Full comparison

```
{
  "schema_version": "2.0",
  "baseline_run_id": "run-6284122a-7a08-44c7-b5c5-363241c66fe9",
  "eia_run_id": "run-4cdee06e-089f-4c1d-944c-30b71e1f903b",
  "release_id": "R2.0",
  "release_build": "R2.2.9.19",
  "runtime_profile_id": "current-poc",
  "runtime_profile_label": "Current POC · 3.1.0-RC10.4",
  "workload_contract": {
    "workload_case_id": "case-5ee2544643c7efb34b09",
    "runtime_profile_id": "current-poc",
    "baseline_scope": {
      "runtime_profile_id": "current-poc",
      "agent_id": "custom_st22_agent",
      "system_id": "PAL",
      "service_id": "custom_st22_agent_service",
      "entity_set": "DumpHeader",
      "reasoning_mode": "LLM_ASSISTED",
      "prompt": "Analyze the selected ST22 evidence. Separate confirmed SAP facts, deterministic findings, likely interpretation, missing evidence and safe next actions.",
      "top": 100,
      "from_date": "",
      "to_date": "",
      "filters": {}
    },
    "candidate_scope": {
      "runtime_profile_id": "current-poc",
      "agent_id": "custom_st22_agent",
      "system_id": "PAL",
      "service_id": "custom_st22_agent_service",
      "entity_set": "DumpHeader",
      "reasoning_mode": "LLM_ASSISTED",
      "prompt": "Analyze the selected ST22 evidence. Separate confirmed SAP facts, deterministic findings, likely interpretation, missing evidence and safe next actions.",
      "top": 100,
      "from_date": "",
      "to_date": "",
      "filters": {}
    },
    "field_checks": {
      "runtime_profile_id": {
        "baseline": "current-poc",
        "with_eia": "current-poc",
        "match": true
      },
      "agent_id": {
        "baseline": "custom_st22_agent",
        "with_eia": "custom_st22_agent",
        "match": true
      },
      "system_id": {
        "baseline": "PAL",
        "with_eia": "PAL",
        "match": true
      },
      "service_id": {
        "baseline": "custom_st22_agent_service",
        "with_eia": "custom_st22_agent_service",
        "match": true
      },
      "entity_set": {
        "baseline": "DumpHeader",
        "with_eia": "DumpHeader",
        "match": true
      },
      "reasoning_mode": {
        "baseline": "LLM_ASSISTED",
        "with_eia": "LLM_ASSISTED",
        "match": true
      },
      "prompt": {
        "baseline": "Analyze the selected ST22 evidence. Separate confirmed SAP facts, deterministic findings, likely interpretation, missing evidence and safe next actions.",
        "with_eia": "Analyze the selected ST22 evidence. Separate confirmed SAP facts, deterministic findings, likely interpretation, missing evidence and safe next actions.",
        "match": true
      },
      "top": {
        "baseline": 100,
        "with_eia": 100,
        "match": true
      },
      "from_date": {
        "baseline": "",
        "with_eia": "",
        "match": true
      },
      "to_date": {
        "baseline": "",
        "with_eia": "",
        "match": true
      },
      "filters": {
        "baseline": {},
        "with_eia": {},
        "match": true
      }
    },
    "all_pinned": true
  },
  "sample_protocol": {
    "runtime_profile_id": "current-poc",
    "baseline_runs": 1,
    "eia_runs": 1,
    "paired_runs": 1,
    "functional_floor": 30,
    "latency_floor": 100,
    "protocol_state": "EVALUATION_ONLY",
    "functional_floor_met": false,
    "latency_floor_met": false,
    "statistical_floor_met": false,
    "signed_approval_required": true,
    "customer_claim_permitted": false,
    "claim_permitted": false,
    "claim_block_reason": "Named Test Automation Architect and Product/Architecture Owner approval is required even after sample floors are met."
  },
  "claim_state": "EVALUATION_ONLY",
  "same_profile": true,
  "same_agent": true,
  "same_system": true,
  "input_parity": true,
  "evidence_changed": true,
  "output_changed": true,
  "baseline": {
    "status": "SUCCESS",
    "mode": "disabled",
    "evidence_hash": "757be9d4c3bc3ed0d2b2312d95221ec7bc706ffa8653b9c334ac8f35f11f13b4",
    "output_hash": "0296f6f00db3be2e22fc4695fecb10453c03ed8a0c612922178070bc2d0f34dd",
    "findings": 6,
    "actions": 0,
    "evidence_profile": {
      "raw_records": 100,
      "unique_records": 100,
      "duplicates_removed": 0,
      "conflicts": 0,
      "coverage": {
        "count": 0,
        "authoritative": 0,
        "supporting": 0
      },
      "mandatory_required": null,
      "mandatory_satisfied": null,
      "raw_bytes": 39579,
      "compact_bytes": 11960,
      "estimated_raw_tokens": 9895,
      "estimated_compact_tokens": 2990,
      "estimated_payload_reduction_pct": 69.8,
      "measurement_note": "Counts use stored run evidence where available. Token values are transparent 4-bytes-per-token estimates, not provider billing data. Missing fields remain null."
    }
  },
  "with_eia": {
    "status": "SUCCESS",
    "mode": "passthrough",
    "alignment_id": "rv-217c1ba00e46d58e",
    "evidence_hash": "d9a5b5da3af860dade34360c2fd264aa46087a62215a915ea3f10a31d1784358",
    "output_hash": "b7dabc5fa15a510914338a821bbbb440cdd19fca8e5a3d2d8d432e3cd2bfd78f",
    "findings": 6,
    "actions": 0,
    "overhead_ms": 8450.429,
    "selected_tools": [],
    "selected_routes": [
      {
        "service_id": "custom_st22_agent_service",
        "entity_set": "DumpHeader",
        "system_id": "PAL"
      }
    ],
    "retrieval_strategy": {},
    "vector_filters": {},
    "evidence_profile": {
      "raw_records": 100,
      "unique_records": 100,
      "duplicates_removed": 0,
      "conflicts": 0,
      "coverage": {
        "count": 4,
        "authoritative": 2,
        "supporting": 2
      },
      "mandatory_required": null,
      "mandatory_satisfied": null,
      "raw_bytes": 38899,
      "compact_bytes": 1629,
      "estimated_raw_tokens": 9725,
      "estimated_compact_tokens": 408,
      "estimated_payload_reduction_pct": 95.8,
      "measurement_note": "Counts use stored run evidence where available. Token values are transparent 4-bytes-per-token estimates, not provider billing data. Missing fields remain null."
    }
  },
  "changes": {
    "tools": [],
    "routes": [
      {
        "service_id": "custom_st22_agent_service",
        "entity_set": "DumpHeader",
        "system_id": "PAL"
      }
    ],
    "retrieval": {},
    "vector_filters": {},
    "evidence_coverage": {
      "count": 4,
      "authoritative": 2,
      "supporting": 2
    },
    "fallback_reason": ""
  },
  "selective_invocation": {
    "recommended_path": "BALANCED",
    "recommended_mode": "Balanced",
    "yes_count": 3,
    "signal_count": 4,
    "signals": [
      {
        "id": "MULTI_SOURCE",
        "label": "Multiple SAP or knowledge sources required",
        "yes": true,
        "evidence": "Route:c6f14c11, SAP"
      },
      {
        "id": "EVIDENCE_UNCERTAINTY",
        "label": "Evidence may be missing, stale or contradictory",
        "yes": true,
        "evidence": "Evidence gap, freshness or conflict signal detected"
      },
      {
        "id": "DECISION_RISK",
        "label": "Decision has operational, financial or compliance risk",
        "yes": false,
        "evidence": "Low-risk context"
      },
      {
        "id": "PORTFOLIO_REUSE",
        "label": "Capability or policy can be reused across agents",
        "yes": true,
        "evidence": "Admitted reusable skill/policy contract"
      }
    ],
    "score": 3,
    "scoring_model": "Four binary signals; no weights",
    "reasons": [
      "Multiple SAP or knowledge sources required",
      "Evidence may be missing, stale or contradictory",
      "Capability or policy can be reused across agents"
    ],
    "statement": "Use bounded evidence validation and context preparation.",
    "advisory_only": true
  },
  "trust_case": {
    "enterprise_truth_owner": "SAP and registered enterprise sources",
    "agent_role": "Orchestrates the task and owns the final response",
    "eia_role": "Validates, deduplicates, correlates and traces evidence before model reasoning",
    "llm_role": "Interpretation, explanation and decision support only",
    "deterministic_outside_llm": [
      "identity and tenant validation",
      "skill and MCP admission",
      "source authority",
      "evidence integrity",
      "mandatory evidence floor",
      "route and policy gates"
    ],
    "proof": {
      "input_parity": "PASS",
      "evidence_trace_id": "9059c404-2fb7-4c3a-8ae8-9e995615b977",
      "alignment_id": "rv-217c1ba00e46d58e",
      "source_routes": [
        {
          "service_id": "custom_st22_agent_service",
          "entity_set": "DumpHeader",
          "system_id": "PAL"
        }
      ],
      "tools": [],
      "coverage": {
        "count": 4,
        "authoritative": 2,
        "supporting": 2
      },
      "payload_reduction_pct": 95.8,
      "overhead_ms": 8450.429,
      "fallback_reason": ""
    }
  },
  "impact_matrix": {
    "schema_version": "1.0",
    "use_case_fit": {
      "recommended_path": "BALANCED",
      "recommended_mode": "Balanced",
      "yes_count": 3,
      "signal_count": 4,
      "signals": [
        {
          "id": "MULTI_SOURCE",
          "label": "Multiple SAP or knowledge sources required",
          "yes": true,
          "evidence": "Route:c6f14c11, SAP"
        },
        {
          "id": "EVIDENCE_UNCERTAINTY",
          "label": "Evidence may be missing, stale or contradictory",
          "yes": true,
          "evidence": "Evidence gap, freshness or conflict signal detected"
        },
        {
          "id": "DECISION_RISK",
          "label": "Decision has operational, financial or compliance risk",
          "yes": false,
          "evidence": "Low-risk context"
        },
        {
          "id": "PORTFOLIO_REUSE",
          "label": "Capability or policy can be reused across agents",
          "yes": true,
          "evidence": "Admitted reusable skill/policy contract"
        }
      ],
      "score": 3,
      "scoring_model": "Four binary signals; no weights",
      "reasons": [
        "Multiple SAP or knowledge sources required",
        "Evidence may be missing, stale or contradictory",
        "Capability or policy can be reused across agents"
      ],
      "statement": "Use bounded evidence validation and context preparation.",
      "advisory_only": true
    },
    "measures": [
      {
        "measure": "Outcome quality",
        "without_eia": "70.0/100",
        "with_eia": "70.0/100",
        "delta": "+0.0",
        "decision": "Pass",
        "basis": "result confidence / result confidence"
      },
      {
        "measure": "Mandatory evidence coverage",
        "without_eia": "Not measured",
        "with_eia": "Not measured",
        "delta": "Not measured",
        "decision": "Fail",
        "basis": "EIA_EVIDENCE_CONTRACT"
      },
      {
        "measure": "Context efficiency",
        "without_eia": "~9895 tokens",
        "with_eia": "~408 tokens",
        "delta": "-9487 tokens",
        "decision": "Better",
        "basis": "Transparent 4-bytes-per-token estimate"
      },
      {
        "measure": "End-to-end latency",
        "without_eia": "Not measured",
        "with_eia": "8450.4 ms EIA overhead",
        "delta": "+8450.4 ms overhead",
        "decision": "High",
        "basis": "not measured / not measured; budget 500 ms"
      },
      {
        "measure": "Trace and fallback",
        "without_eia": "Direct trace present",
        "with_eia": "Evidence trace + fallback",
        "delta": "Governed trace added",
        "decision": "Pass",
        "basis": "Evidence/alignment trace and direct fallback policy"
      }
    ],
    "final_decision": "EIA Not Justified",
    "requirement_state": "EIA Evaluated",
    "rationale": "Mandatory evidence coverage is below the configured 100% threshold.",
    "configured_thresholds": {
      "mandatory_evidence_coverage_pct": 100,
      "latency_budget_ms": 500
    },
    "security_gate": {
      "decision": "Pass",
      "failed": false,
      "signals": {}
    },
    "pre_deployment_roles": {},
    "rules": {
      "quality_must_not_decrease": true,
      "mandatory_evidence_threshold_required": true,
      "security_failures_are_automatic": true,
      "token_reduction_alone_is_not_beneficial": true,
      "simple_use_cases_may_bypass": true
    }
  },
  "release_aware_report": {
    "schema_version": "2.0",
    "release_id": "R2.0",
    "release_build": "R2.2.9.19",
    "eia_version": "0.4.0",
    "release_outcome": "Controlled optimization and measurable value integrated with Agent Hub",
    "release_awareness": {
      "current_release": "Release 2",
      "p4_p5_active": true,
      "states": [
        "Advisory",
        "Blocked",
        "Disabled by Policy",
        "Insufficient Evidence",
        "Measured",
        "Not Activated",
        "Not Available in Current Release",
        "Observed"
      ],
      "rule": "Unsupported metrics are never represented as zero, failed or proven."
    },
    "classification": "Trust Improvement Observed",
    "future_classification": {
      "label": "Enterprise Value Proven",
      "status": "Available only after sample floors and named approval",
      "available_after": "30 functional pairs, 100 latency pairs and signed G6 evidence",
      "current_observation": "Portfolio Reuse Identified"
    },
    "dimensions": [
      {
        "dimension": "Trust & Output",
        "direct_agent_hub": {
          "quality": "70.0/100",
          "mandatory_evidence": "Not measured"
        },
        "eia": {
          "quality": "70.0/100",
          "mandatory_evidence": "Not measured"
        },
        "delta": "Quality +0.0; evidence Not measured",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 supports trust, traceability and output-parity observation; measured output improvement requires P4/P5.",
          "release": "Release 2"
        },
        "classification": "Trust Improvement Observed",
        "explanation": "Shows evidence completeness, traceability and non-degradation without claiming active optimization.",
        "fully_measurable_release": "P4/P5"
      },
      {
        "dimension": "Runtime Performance",
        "direct_agent_hub": "Not measured",
        "eia": {
          "end_to_end": "Not measured",
          "synchronous_overhead": "8450.429 ms"
        },
        "delta": "Not measured",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 measures overhead where trace timing exists; net acceleration is a P4/P5 outcome.",
          "release": "Release 2"
        },
        "classification": "Observed overhead",
        "explanation": "Separates Microkernel coordination from SAP, MCP, retrieval, vector and LLM wait.",
        "fully_measurable_release": "P4/P5"
      },
      {
        "dimension": "Resilience",
        "direct_agent_hub": "Direct fallback policy",
        "eia": "No repair/fallback activated",
        "delta": "Not activated",
        "availability": {
          "state": "Not Activated",
          "reason": "Release 2 may observe repair and fallback readiness but does not auto-apply recovery.",
          "release": "Release 2"
        },
        "classification": "Neutral",
        "explanation": "Reports repair recommendation, fallback readiness and failure handling without mutating live execution.",
        "fully_measurable_release": "P5"
      },
      {
        "dimension": "Enterprise Value",
        "direct_agent_hub": "Per-agent configuration",
        "eia": "Shared Release 2 admission/evidence contract",
        "delta": "9 agents identified",
        "availability": {
          "state": "Observed",
          "reason": "Release 2 can identify reuse; portfolio economics and change-effort reduction require P5 benchmark evidence.",
          "release": "Release 2"
        },
        "classification": "Portfolio Reuse Identified",
        "explanation": "Identifies shared governed assets without presenting financial ROI as proven.",
        "fully_measurable_release": "P5"
      }
    ],
    "paired_comparison": [
      {
        "measure": "Outcome quality",
        "direct_agent_hub": "70.0/100",
        "eia": "70.0/100",
        "delta": "+0.0",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 may observe parity or quality signals, but controlled optimization improvement is a P4/P5 claim.",
          "release": "P4/P5"
        },
        "classification": "Pass",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "Mandatory evidence coverage",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "Coverage is derived from the persisted evidence contract; Pre-Deployment uses Primary, ATC, Tests, Dependency and Transport.",
          "release": "Release 2"
        },
        "classification": "Fail",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Unsupported critical claims",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "A value is shown only when the claim-validation trace records unsupported critical claims.",
          "release": "Release 2"
        },
        "classification": "Not proven",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Context size or input tokens",
        "direct_agent_hub": "~9895",
        "eia": "~408",
        "delta": "-9487",
        "availability": {
          "state": "Observed",
          "reason": "Context values are transparent estimates and cannot alone establish benefit; paired quality and evidence floors remain mandatory.",
          "release": "P4/P5"
        },
        "classification": "Observed only",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "Tool and retrieval calls",
        "direct_agent_hub": 0,
        "eia": 0,
        "delta": 0,
        "availability": {
          "state": "Observed",
          "reason": "Release 2 records and may deterministically curate selected tools, routes and retrieval within the approved optimization boundary.",
          "release": "P4/P5"
        },
        "classification": "Observed only",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "End-to-end latency",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "Paired persisted timings are required; optimization claims remain gated.",
          "release": "P4/P5"
        },
        "classification": "Not proven",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "EIA synchronous overhead",
        "direct_agent_hub": "N/A",
        "eia": "8450.429 ms",
        "delta": "8450.429 ms",
        "availability": {
          "state": "Measured",
          "reason": "Only thin synchronous EIA coordination is included; external and LLM time is excluded.",
          "release": "Release 2"
        },
        "classification": "Acceptable",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Repair and fallback success",
        "direct_agent_hub": "Direct fallback only",
        "eia": "Not activated",
        "delta": "Not activated",
        "availability": {
          "state": "Not Activated",
          "reason": "Release 2 may recommend repair or prove fallback readiness without changing live output.",
          "release": "P5"
        },
        "classification": "Not activated",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Cost per successful task",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires full runtime, control-plane, evaluation, storage and operations cost with successful-task denominator.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Reusable agents affected",
        "direct_agent_hub": "Not measured",
        "eia": 9,
        "delta": "Identified, not financially proven",
        "availability": {
          "state": "Observed",
          "reason": "Release 2 may identify shared governed capability, policy or evidence contracts; economics remain unproven.",
          "release": "P5"
        },
        "classification": "Portfolio Reuse Identified",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Engineering effort saved",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires controlled portfolio delivery baselines and engineering-hour evidence.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Shared-change effort saved",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires a certified shared change, impacted-agent set and measured regression effort.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Incident effort avoided",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires incident baseline, recovery outcome and avoided-effort evidence.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      }
    ],
    "functional_decisions": [
      {
        "question": "Did EIA improve trust?",
        "answer": "Observed only",
        "reason": "Trust Improvement Observed"
      },
      {
        "question": "Did EIA change the final result?",
        "answer": "Yes",
        "reason": "Optimize may change bounded context or tool selection; Agent Hub still owns workflow state and the final response."
      },
      {
        "question": "Was mandatory evidence complete?",
        "answer": "Not measured",
        "reason": "No configured role missing"
      },
      {
        "question": "Did EIA introduce material overhead?",
        "answer": "8450.429 ms",
        "reason": "Microkernel-only synchronous overhead"
      },
      {
        "question": "Did EIA improve resilience?",
        "answer": "No activation",
        "reason": "No classified failure"
      },
      {
        "question": "Was EIA necessary for this workload?",
        "answer": "Yes",
        "reason": "Use bounded evidence validation and context preparation."
      },
      {
        "question": "Can the same capability benefit other agents?",
        "answer": "9",
        "reason": "Shared Release 2 admission/evidence contract"
      },
      {
        "question": "Has optimization value been proven?",
        "answer": "Not yet",
        "reason": "Release 2 enables measurement; proof still requires paired sample floors, quality/evidence floors and signed G6 evidence."
      },
      {
        "question": "Has enterprise economic value been proven?",
        "answer": "Not yet",
        "reason": "Portfolio economics requires a signed P5/G6 benchmark and named approval."
      }
    ],
    "qualitative_explanation": "EIA was evaluated because 3 of 4 use-case-fit signals were present and recommended Balanced mode. Mandatory evidence was evaluated against the configured evidence contract. No configured mandatory role was recorded as missing. Governed sources considered: Route:c6f14c11, SAP. EIA recommendation: Continue with governed evidence. The recommendation did not change live execution because Release 2 is advisory in shadow/passthrough mode. Trust improvement was observed. Optimize may run within the approved deterministic boundary, but enterprise economic value cannot be claimed until the paired sample floors and named G6 approvals are complete.",
    "sap_evidence": {
      "applicable": false,
      "state": "Not Activated",
      "reason": "The selected run is not the Pre-Deployment Check Agent."
    },
    "technical_execution": {
      "runtime_microkernel": {
        "eia_release_and_version": "R2.0 / 0.4.0",
        "active_mode": "passthrough",
        "suitability_recommendation": "BALANCED",
        "runtime_microkernel_overhead_ms": 8450.429,
        "total_synchronous_eia_time_ms": 8450.429,
        "external_sap_wait_ms": null,
        "mcp_wait_ms": null,
        "rag_vector_wait_ms": null,
        "llm_time_ms": null,
        "cache_state_and_hit": "Not recorded",
        "resolved_profile_and_version": "Not recorded / Not recorded",
        "runtime_guard_decision": "Pass",
        "evidence_decision": "Continue",
        "fallback_used": "No",
        "trace_id": "9059c404-2fb7-4c3a-8ae8-9e995615b977",
        "measurement_rule": "Microkernel overhead excludes SAP, MCP, RAG, vector, LLM and asynchronous telemetry time."
      },
      "latency_decomposition": {
        "microkernel_overhead_ms": 8450.429,
        "total_synchronous_eia_ms": 8450.429,
        "external_sap_wait_ms": null,
        "mcp_wait_ms": null,
        "rag_wait_ms": null,
        "vector_wait_ms": null,
        "llm_time_ms": null,
        "end_to_end_ms": null,
        "end_to_end_source": "not measured",
        "external_time_excluded_from_microkernel": true,
        "decomposition_complete": false
      },
      "optimization_cells": [
        {
          "cell": "Suitability & Bypass",
          "release_availability": "Release 2",
          "activation_reason": "3 of 4 signals; BALANCED recommended",
          "duration_ms": null,
          "result": "BALANCED",
          "state": "Observed",
          "state_reason": "Release 2 evaluates suitability without changing live execution.",
          "input_count": 4,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use bounded evidence validation and context preparation.",
          "fallback_action": "",
          "error_or_hard_stop": "",
          "kill_switch_state": "Mode override available"
        },
        {
          "cell": "Profile Resolution",
          "release_availability": "Release 2",
          "activation_reason": "Non-bypass request",
          "duration_ms": null,
          "result": "Not recorded / Not recorded",
          "state": "Insufficient Evidence",
          "state_reason": "No resolved-profile identifier was persisted for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use the current certified profile or safe bypass.",
          "fallback_action": "Previous certified view or safe bypass",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Capability Resolution",
          "release_availability": "Release 2",
          "activation_reason": "Enterprise capability required",
          "duration_ms": null,
          "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
          "state": "Observed",
          "state_reason": "Certified route/capability candidates were recorded.",
          "input_count": 1,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use certified route only",
          "fallback_action": "Next certified route or structured gap",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Skill and MCP Admission",
          "release_availability": "Release 2",
          "activation_reason": "No MCP tool required",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No MCP tool was selected for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Admit only certified read-only tools",
          "fallback_action": "Certified direct safe set",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Data Quality",
          "release_availability": "Release 2",
          "activation_reason": "New enterprise evidence object",
          "duration_ms": null,
          "result": "100 unique; 0 duplicates removed",
          "state": "Observed",
          "state_reason": "Persisted evidence counts support an observed quality review.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Conflicts: 0",
          "recommendation": "",
          "fallback_action": "Quarantine weak evidence",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Policy & Masking",
          "release_availability": "Release 2",
          "activation_reason": "Mandatory before data leaves trust boundary",
          "duration_ms": null,
          "result": "Not fully evidenced",
          "state": "Insufficient Evidence",
          "state_reason": "No detailed policy/masking trace was persisted.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Fail closed; no direct fallback",
          "error_or_hard_stop": "",
          "kill_switch_state": "Emergency deny-all available"
        },
        {
          "cell": "Evidence & Trust",
          "release_availability": "Release 2",
          "activation_reason": "Every factual output package",
          "duration_ms": null,
          "result": "Continue",
          "state": "Observed",
          "state_reason": "Evidence trace and coverage are available.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Mandatory coverage: Not measured",
          "recommendation": "Continue",
          "fallback_action": "Mark unverified; block when evidence floor is unmet",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Recovery & Resilience",
          "release_availability": "Release 2",
          "activation_reason": "No classified failure",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No classified failure required recovery for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified fallback available by policy",
          "error_or_hard_stop": "",
          "kill_switch_state": "Force bypass available"
        },
        {
          "cell": "Data Acquisition Optimization",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
          "state": "Not Activated",
          "state_reason": "Optimize was not active or no route decision was required.",
          "input_count": 1,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified alternate route or direct safe path",
          "error_or_hard_stop": "",
          "kill_switch_state": "Source circuit breaker available"
        },
        {
          "cell": "MCP Tool Curation",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "Optimize was not active or no tool curation was required.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified direct safe set",
          "error_or_hard_stop": "",
          "kill_switch_state": "Tool curation can be disabled"
        },
        {
          "cell": "Retrieval Strategy Optimization",
          "release_availability": "P4",
          "activation_reason": "No retrieval optimization required",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No optimized retrieval strategy was recorded.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Exact or sparse retrieval, otherwise declare evidence gap",
          "error_or_hard_stop": "",
          "kill_switch_state": "Retrieval namespace can be disabled"
        },
        {
          "cell": "Vector Health and Routing",
          "release_availability": "P4",
          "activation_reason": "Vector path not selected",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "Vector routing was not selected for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Parent namespace or non-vector retrieval",
          "error_or_hard_stop": "",
          "kill_switch_state": "Vector namespace quarantine available"
        },
        {
          "cell": "Context Optimization",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "1629.0 bytes",
          "state": "Not Activated",
          "state_reason": "No optimized context package was recorded.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Estimated compact tokens: 408",
          "recommendation": "",
          "fallback_action": "Compress optional content; preserve policy/evidence floor",
          "error_or_hard_stop": "",
          "kill_switch_state": "Certified context template available"
        },
        {
          "cell": "Performance and Cost Evaluation",
          "release_availability": "P5",
          "activation_reason": "Every controlled evaluation run",
          "duration_ms": 8450.429,
          "result": "8450.4 ms",
          "state": "Observed",
          "state_reason": "Run-level overhead was measured; cohort claims still require paired sample floors.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Aggregate only within the same pinned workload and cache-state cohort.",
          "fallback_action": "Retain local ledger when export is unavailable",
          "error_or_hard_stop": "",
          "kill_switch_state": "Metric export can be disabled without blocking execution"
        },
        {
          "cell": "Portfolio Economics",
          "release_availability": "P5",
          "activation_reason": "After paired functional and latency cohorts",
          "duration_ms": null,
          "result": "Awaiting 30/100 paired cohorts and named approval",
          "state": "Insufficient Evidence",
          "state_reason": "Release 2 can collect reuse and cost evidence, but enterprise-value claims require a signed G6 benchmark.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Do not publish customer ROI or acceleration claims yet.",
          "fallback_action": "Keep the comparison evaluation-only",
          "error_or_hard_stop": "",
          "kill_switch_state": "Claim release gate enforced"
        }
      ],
      "show_relevant_cells_by_default": true,
      "p4_p5_runtime_activated": false,
      "release_gate": "P4/P5 controls are enabled only in Optimize mode. External acceleration claims still require paired sample floors, quality/evidence floors, rollback proof and named G6 approval.",
      "sap_evidence": {
        "applicable": false,
        "state": "Not Activated",
        "reason": "The selected run is not the Pre-Deployment Check Agent."
      }
    },
    "reuse": {
      "reusable_agents_affected": 9,
      "capability_or_policy": "Shared Release 2 admission/evidence contract",
      "identified": true,
      "financially_proven": false
    },
    "release_controls": {
      "mode_mutation_allowed": true,
      "optimize_enabled": true,
      "p4_p5_claims_permitted": false,
      "approved_mutation_boundary": [
        "tool curation",
        "route ranking",
        "retrieval bounds",
        "context budget",
        "evidence hard stop"
      ],
      "claim_requirements": [
        "30 paired functional runs",
        "100 paired latency runs",
        "signed benchmark evidence",
        "quality and evidence floors",
        "rollback and kill switch"
      ]
    }
  },
  "operations_value_matrix": {
    "schema_version": "2.0",
    "release_id": "R2.0",
    "release_build": "R2.2.9.19",
    "eia_version": "0.4.0",
    "release_outcome": "Controlled optimization and measurable value integrated with Agent Hub",
    "release_awareness": {
      "current_release": "Release 2",
      "p4_p5_active": true,
      "states": [
        "Advisory",
        "Blocked",
        "Disabled by Policy",
        "Insufficient Evidence",
        "Measured",
        "Not Activated",
        "Not Available in Current Release",
        "Observed"
      ],
      "rule": "Unsupported metrics are never represented as zero, failed or proven."
    },
    "classification": "Trust Improvement Observed",
    "future_classification": {
      "label": "Enterprise Value Proven",
      "status": "Available only after sample floors and named approval",
      "available_after": "30 functional pairs, 100 latency pairs and signed G6 evidence",
      "current_observation": "Portfolio Reuse Identified"
    },
    "dimensions": [
      {
        "dimension": "Trust & Output",
        "direct_agent_hub": {
          "quality": "70.0/100",
          "mandatory_evidence": "Not measured"
        },
        "eia": {
          "quality": "70.0/100",
          "mandatory_evidence": "Not measured"
        },
        "delta": "Quality +0.0; evidence Not measured",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 supports trust, traceability and output-parity observation; measured output improvement requires P4/P5.",
          "release": "Release 2"
        },
        "classification": "Trust Improvement Observed",
        "explanation": "Shows evidence completeness, traceability and non-degradation without claiming active optimization.",
        "fully_measurable_release": "P4/P5"
      },
      {
        "dimension": "Runtime Performance",
        "direct_agent_hub": "Not measured",
        "eia": {
          "end_to_end": "Not measured",
          "synchronous_overhead": "8450.429 ms"
        },
        "delta": "Not measured",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 measures overhead where trace timing exists; net acceleration is a P4/P5 outcome.",
          "release": "Release 2"
        },
        "classification": "Observed overhead",
        "explanation": "Separates Microkernel coordination from SAP, MCP, retrieval, vector and LLM wait.",
        "fully_measurable_release": "P4/P5"
      },
      {
        "dimension": "Resilience",
        "direct_agent_hub": "Direct fallback policy",
        "eia": "No repair/fallback activated",
        "delta": "Not activated",
        "availability": {
          "state": "Not Activated",
          "reason": "Release 2 may observe repair and fallback readiness but does not auto-apply recovery.",
          "release": "Release 2"
        },
        "classification": "Neutral",
        "explanation": "Reports repair recommendation, fallback readiness and failure handling without mutating live execution.",
        "fully_measurable_release": "P5"
      },
      {
        "dimension": "Enterprise Value",
        "direct_agent_hub": "Per-agent configuration",
        "eia": "Shared Release 2 admission/evidence contract",
        "delta": "9 agents identified",
        "availability": {
          "state": "Observed",
          "reason": "Release 2 can identify reuse; portfolio economics and change-effort reduction require P5 benchmark evidence.",
          "release": "Release 2"
        },
        "classification": "Portfolio Reuse Identified",
        "explanation": "Identifies shared governed assets without presenting financial ROI as proven.",
        "fully_measurable_release": "P5"
      }
    ],
    "paired_comparison": [
      {
        "measure": "Outcome quality",
        "direct_agent_hub": "70.0/100",
        "eia": "70.0/100",
        "delta": "+0.0",
        "availability": {
          "state": "Measured",
          "reason": "Release 2 may observe parity or quality signals, but controlled optimization improvement is a P4/P5 claim.",
          "release": "P4/P5"
        },
        "classification": "Pass",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "Mandatory evidence coverage",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "Coverage is derived from the persisted evidence contract; Pre-Deployment uses Primary, ATC, Tests, Dependency and Transport.",
          "release": "Release 2"
        },
        "classification": "Fail",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Unsupported critical claims",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "A value is shown only when the claim-validation trace records unsupported critical claims.",
          "release": "Release 2"
        },
        "classification": "Not proven",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Context size or input tokens",
        "direct_agent_hub": "~9895",
        "eia": "~408",
        "delta": "-9487",
        "availability": {
          "state": "Observed",
          "reason": "Context values are transparent estimates and cannot alone establish benefit; paired quality and evidence floors remain mandatory.",
          "release": "P4/P5"
        },
        "classification": "Observed only",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "Tool and retrieval calls",
        "direct_agent_hub": 0,
        "eia": 0,
        "delta": 0,
        "availability": {
          "state": "Observed",
          "reason": "Release 2 records and may deterministically curate selected tools, routes and retrieval within the approved optimization boundary.",
          "release": "P4/P5"
        },
        "classification": "Observed only",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "End-to-end latency",
        "direct_agent_hub": "Not measured",
        "eia": "Not measured",
        "delta": "Not measured",
        "availability": {
          "state": "Insufficient Evidence",
          "reason": "Paired persisted timings are required; optimization claims remain gated.",
          "release": "P4/P5"
        },
        "classification": "Not proven",
        "fully_measurable_release": "P4/P5"
      },
      {
        "measure": "EIA synchronous overhead",
        "direct_agent_hub": "N/A",
        "eia": "8450.429 ms",
        "delta": "8450.429 ms",
        "availability": {
          "state": "Measured",
          "reason": "Only thin synchronous EIA coordination is included; external and LLM time is excluded.",
          "release": "Release 2"
        },
        "classification": "Acceptable",
        "fully_measurable_release": "Release 2"
      },
      {
        "measure": "Repair and fallback success",
        "direct_agent_hub": "Direct fallback only",
        "eia": "Not activated",
        "delta": "Not activated",
        "availability": {
          "state": "Not Activated",
          "reason": "Release 2 may recommend repair or prove fallback readiness without changing live output.",
          "release": "P5"
        },
        "classification": "Not activated",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Cost per successful task",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires full runtime, control-plane, evaluation, storage and operations cost with successful-task denominator.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Reusable agents affected",
        "direct_agent_hub": "Not measured",
        "eia": 9,
        "delta": "Identified, not financially proven",
        "availability": {
          "state": "Observed",
          "reason": "Release 2 may identify shared governed capability, policy or evidence contracts; economics remain unproven.",
          "release": "P5"
        },
        "classification": "Portfolio Reuse Identified",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Engineering effort saved",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires controlled portfolio delivery baselines and engineering-hour evidence.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Shared-change effort saved",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires a certified shared change, impacted-agent set and measured regression effort.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      },
      {
        "measure": "Incident effort avoided",
        "direct_agent_hub": "Not available",
        "eia": "Not available",
        "delta": "Not available",
        "availability": {
          "state": "Not Available in Current Release",
          "reason": "Requires incident baseline, recovery outcome and avoided-effort evidence.",
          "release": "P5"
        },
        "classification": "Not available",
        "fully_measurable_release": "P5"
      }
    ],
    "functional_decisions": [
      {
        "question": "Did EIA improve trust?",
        "answer": "Observed only",
        "reason": "Trust Improvement Observed"
      },
      {
        "question": "Did EIA change the final result?",
        "answer": "Yes",
        "reason": "Optimize may change bounded context or tool selection; Agent Hub still owns workflow state and the final response."
      },
      {
        "question": "Was mandatory evidence complete?",
        "answer": "Not measured",
        "reason": "No configured role missing"
      },
      {
        "question": "Did EIA introduce material overhead?",
        "answer": "8450.429 ms",
        "reason": "Microkernel-only synchronous overhead"
      },
      {
        "question": "Did EIA improve resilience?",
        "answer": "No activation",
        "reason": "No classified failure"
      },
      {
        "question": "Was EIA necessary for this workload?",
        "answer": "Yes",
        "reason": "Use bounded evidence validation and context preparation."
      },
      {
        "question": "Can the same capability benefit other agents?",
        "answer": "9",
        "reason": "Shared Release 2 admission/evidence contract"
      },
      {
        "question": "Has optimization value been proven?",
        "answer": "Not yet",
        "reason": "Release 2 enables measurement; proof still requires paired sample floors, quality/evidence floors and signed G6 evidence."
      },
      {
        "question": "Has enterprise economic value been proven?",
        "answer": "Not yet",
        "reason": "Portfolio economics requires a signed P5/G6 benchmark and named approval."
      }
    ],
    "qualitative_explanation": "EIA was evaluated because 3 of 4 use-case-fit signals were present and recommended Balanced mode. Mandatory evidence was evaluated against the configured evidence contract. No configured mandatory role was recorded as missing. Governed sources considered: Route:c6f14c11, SAP. EIA recommendation: Continue with governed evidence. The recommendation did not change live execution because Release 2 is advisory in shadow/passthrough mode. Trust improvement was observed. Optimize may run within the approved deterministic boundary, but enterprise economic value cannot be claimed until the paired sample floors and named G6 approvals are complete.",
    "sap_evidence": {
      "applicable": false,
      "state": "Not Activated",
      "reason": "The selected run is not the Pre-Deployment Check Agent."
    },
    "technical_execution": {
      "runtime_microkernel": {
        "eia_release_and_version": "R2.0 / 0.4.0",
        "active_mode": "passthrough",
        "suitability_recommendation": "BALANCED",
        "runtime_microkernel_overhead_ms": 8450.429,
        "total_synchronous_eia_time_ms": 8450.429,
        "external_sap_wait_ms": null,
        "mcp_wait_ms": null,
        "rag_vector_wait_ms": null,
        "llm_time_ms": null,
        "cache_state_and_hit": "Not recorded",
        "resolved_profile_and_version": "Not recorded / Not recorded",
        "runtime_guard_decision": "Pass",
        "evidence_decision": "Continue",
        "fallback_used": "No",
        "trace_id": "9059c404-2fb7-4c3a-8ae8-9e995615b977",
        "measurement_rule": "Microkernel overhead excludes SAP, MCP, RAG, vector, LLM and asynchronous telemetry time."
      },
      "latency_decomposition": {
        "microkernel_overhead_ms": 8450.429,
        "total_synchronous_eia_ms": 8450.429,
        "external_sap_wait_ms": null,
        "mcp_wait_ms": null,
        "rag_wait_ms": null,
        "vector_wait_ms": null,
        "llm_time_ms": null,
        "end_to_end_ms": null,
        "end_to_end_source": "not measured",
        "external_time_excluded_from_microkernel": true,
        "decomposition_complete": false
      },
      "optimization_cells": [
        {
          "cell": "Suitability & Bypass",
          "release_availability": "Release 2",
          "activation_reason": "3 of 4 signals; BALANCED recommended",
          "duration_ms": null,
          "result": "BALANCED",
          "state": "Observed",
          "state_reason": "Release 2 evaluates suitability without changing live execution.",
          "input_count": 4,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use bounded evidence validation and context preparation.",
          "fallback_action": "",
          "error_or_hard_stop": "",
          "kill_switch_state": "Mode override available"
        },
        {
          "cell": "Profile Resolution",
          "release_availability": "Release 2",
          "activation_reason": "Non-bypass request",
          "duration_ms": null,
          "result": "Not recorded / Not recorded",
          "state": "Insufficient Evidence",
          "state_reason": "No resolved-profile identifier was persisted for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use the current certified profile or safe bypass.",
          "fallback_action": "Previous certified view or safe bypass",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Capability Resolution",
          "release_availability": "Release 2",
          "activation_reason": "Enterprise capability required",
          "duration_ms": null,
          "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
          "state": "Observed",
          "state_reason": "Certified route/capability candidates were recorded.",
          "input_count": 1,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Use certified route only",
          "fallback_action": "Next certified route or structured gap",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Skill and MCP Admission",
          "release_availability": "Release 2",
          "activation_reason": "No MCP tool required",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No MCP tool was selected for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Admit only certified read-only tools",
          "fallback_action": "Certified direct safe set",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Data Quality",
          "release_availability": "Release 2",
          "activation_reason": "New enterprise evidence object",
          "duration_ms": null,
          "result": "100 unique; 0 duplicates removed",
          "state": "Observed",
          "state_reason": "Persisted evidence counts support an observed quality review.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Conflicts: 0",
          "recommendation": "",
          "fallback_action": "Quarantine weak evidence",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Policy & Masking",
          "release_availability": "Release 2",
          "activation_reason": "Mandatory before data leaves trust boundary",
          "duration_ms": null,
          "result": "Not fully evidenced",
          "state": "Insufficient Evidence",
          "state_reason": "No detailed policy/masking trace was persisted.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Fail closed; no direct fallback",
          "error_or_hard_stop": "",
          "kill_switch_state": "Emergency deny-all available"
        },
        {
          "cell": "Evidence & Trust",
          "release_availability": "Release 2",
          "activation_reason": "Every factual output package",
          "duration_ms": null,
          "result": "Continue",
          "state": "Observed",
          "state_reason": "Evidence trace and coverage are available.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Mandatory coverage: Not measured",
          "recommendation": "Continue",
          "fallback_action": "Mark unverified; block when evidence floor is unmet",
          "error_or_hard_stop": "",
          "kill_switch_state": "Available"
        },
        {
          "cell": "Recovery & Resilience",
          "release_availability": "Release 2",
          "activation_reason": "No classified failure",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No classified failure required recovery for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified fallback available by policy",
          "error_or_hard_stop": "",
          "kill_switch_state": "Force bypass available"
        },
        {
          "cell": "Data Acquisition Optimization",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
          "state": "Not Activated",
          "state_reason": "Optimize was not active or no route decision was required.",
          "input_count": 1,
          "output_count": 1,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified alternate route or direct safe path",
          "error_or_hard_stop": "",
          "kill_switch_state": "Source circuit breaker available"
        },
        {
          "cell": "MCP Tool Curation",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "Optimize was not active or no tool curation was required.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Certified direct safe set",
          "error_or_hard_stop": "",
          "kill_switch_state": "Tool curation can be disabled"
        },
        {
          "cell": "Retrieval Strategy Optimization",
          "release_availability": "P4",
          "activation_reason": "No retrieval optimization required",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "No optimized retrieval strategy was recorded.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Exact or sparse retrieval, otherwise declare evidence gap",
          "error_or_hard_stop": "",
          "kill_switch_state": "Retrieval namespace can be disabled"
        },
        {
          "cell": "Vector Health and Routing",
          "release_availability": "P4",
          "activation_reason": "Vector path not selected",
          "duration_ms": null,
          "result": "Not activated",
          "state": "Not Activated",
          "state_reason": "Vector routing was not selected for this run.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "",
          "fallback_action": "Parent namespace or non-vector retrieval",
          "error_or_hard_stop": "",
          "kill_switch_state": "Vector namespace quarantine available"
        },
        {
          "cell": "Context Optimization",
          "release_availability": "P4",
          "activation_reason": "Optimize mode not active",
          "duration_ms": null,
          "result": "1629.0 bytes",
          "state": "Not Activated",
          "state_reason": "No optimized context package was recorded.",
          "input_count": 100,
          "output_count": 100,
          "budget_used": null,
          "evidence_actions": "Estimated compact tokens: 408",
          "recommendation": "",
          "fallback_action": "Compress optional content; preserve policy/evidence floor",
          "error_or_hard_stop": "",
          "kill_switch_state": "Certified context template available"
        },
        {
          "cell": "Performance and Cost Evaluation",
          "release_availability": "P5",
          "activation_reason": "Every controlled evaluation run",
          "duration_ms": 8450.429,
          "result": "8450.4 ms",
          "state": "Observed",
          "state_reason": "Run-level overhead was measured; cohort claims still require paired sample floors.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Aggregate only within the same pinned workload and cache-state cohort.",
          "fallback_action": "Retain local ledger when export is unavailable",
          "error_or_hard_stop": "",
          "kill_switch_state": "Metric export can be disabled without blocking execution"
        },
        {
          "cell": "Portfolio Economics",
          "release_availability": "P5",
          "activation_reason": "After paired functional and latency cohorts",
          "duration_ms": null,
          "result": "Awaiting 30/100 paired cohorts and named approval",
          "state": "Insufficient Evidence",
          "state_reason": "Release 2 can collect reuse and cost evidence, but enterprise-value claims require a signed G6 benchmark.",
          "input_count": null,
          "output_count": null,
          "budget_used": null,
          "evidence_actions": "",
          "recommendation": "Do not publish customer ROI or acceleration claims yet.",
          "fallback_action": "Keep the comparison evaluation-only",
          "error_or_hard_stop": "",
          "kill_switch_state": "Claim release gate enforced"
        }
      ],
      "show_relevant_cells_by_default": true,
      "p4_p5_runtime_activated": false,
      "release_gate": "P4/P5 controls are enabled only in Optimize mode. External acceleration claims still require paired sample floors, quality/evidence floors, rollback proof and named G6 approval.",
      "sap_evidence": {
        "applicable": false,
        "state": "Not Activated",
        "reason": "The selected run is not the Pre-Deployment Check Agent."
      }
    },
    "reuse": {
      "reusable_agents_affected": 9,
      "capability_or_policy": "Shared Release 2 admission/evidence contract",
      "identified": true,
      "financially_proven": false
    },
    "release_controls": {
      "mode_mutation_allowed": true,
      "optimize_enabled": true,
      "p4_p5_claims_permitted": false,
      "approved_mutation_boundary": [
        "tool curation",
        "route ranking",
        "retrieval bounds",
        "context budget",
        "evidence hard stop"
      ],
      "claim_requirements": [
        "30 paired functional runs",
        "100 paired latency runs",
        "signed benchmark evidence",
        "quality and evidence floors",
        "rollback and kill switch"
      ]
    }
  },
  "technical_execution": {
    "runtime_microkernel": {
      "eia_release_and_version": "R2.0 / 0.4.0",
      "active_mode": "passthrough",
      "suitability_recommendation": "BALANCED",
      "runtime_microkernel_overhead_ms": 8450.429,
      "total_synchronous_eia_time_ms": 8450.429,
      "external_sap_wait_ms": null,
      "mcp_wait_ms": null,
      "rag_vector_wait_ms": null,
      "llm_time_ms": null,
      "cache_state_and_hit": "Not recorded",
      "resolved_profile_and_version": "Not recorded / Not recorded",
      "runtime_guard_decision": "Pass",
      "evidence_decision": "Continue",
      "fallback_used": "No",
      "trace_id": "9059c404-2fb7-4c3a-8ae8-9e995615b977",
      "measurement_rule": "Microkernel overhead excludes SAP, MCP, RAG, vector, LLM and asynchronous telemetry time."
    },
    "latency_decomposition": {
      "microkernel_overhead_ms": 8450.429,
      "total_synchronous_eia_ms": 8450.429,
      "external_sap_wait_ms": null,
      "mcp_wait_ms": null,
      "rag_wait_ms": null,
      "vector_wait_ms": null,
      "llm_time_ms": null,
      "end_to_end_ms": null,
      "end_to_end_source": "not measured",
      "external_time_excluded_from_microkernel": true,
      "decomposition_complete": false
    },
    "optimization_cells": [
      {
        "cell": "Suitability & Bypass",
        "release_availability": "Release 2",
        "activation_reason": "3 of 4 signals; BALANCED recommended",
        "duration_ms": null,
        "result": "BALANCED",
        "state": "Observed",
        "state_reason": "Release 2 evaluates suitability without changing live execution.",
        "input_count": 4,
        "output_count": 1,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Use bounded evidence validation and context preparation.",
        "fallback_action": "",
        "error_or_hard_stop": "",
        "kill_switch_state": "Mode override available"
      },
      {
        "cell": "Profile Resolution",
        "release_availability": "Release 2",
        "activation_reason": "Non-bypass request",
        "duration_ms": null,
        "result": "Not recorded / Not recorded",
        "state": "Insufficient Evidence",
        "state_reason": "No resolved-profile identifier was persisted for this run.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Use the current certified profile or safe bypass.",
        "fallback_action": "Previous certified view or safe bypass",
        "error_or_hard_stop": "",
        "kill_switch_state": "Available"
      },
      {
        "cell": "Capability Resolution",
        "release_availability": "Release 2",
        "activation_reason": "Enterprise capability required",
        "duration_ms": null,
        "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
        "state": "Observed",
        "state_reason": "Certified route/capability candidates were recorded.",
        "input_count": 1,
        "output_count": 1,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Use certified route only",
        "fallback_action": "Next certified route or structured gap",
        "error_or_hard_stop": "",
        "kill_switch_state": "Available"
      },
      {
        "cell": "Skill and MCP Admission",
        "release_availability": "Release 2",
        "activation_reason": "No MCP tool required",
        "duration_ms": null,
        "result": "Not activated",
        "state": "Not Activated",
        "state_reason": "No MCP tool was selected for this run.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Admit only certified read-only tools",
        "fallback_action": "Certified direct safe set",
        "error_or_hard_stop": "",
        "kill_switch_state": "Available"
      },
      {
        "cell": "Data Quality",
        "release_availability": "Release 2",
        "activation_reason": "New enterprise evidence object",
        "duration_ms": null,
        "result": "100 unique; 0 duplicates removed",
        "state": "Observed",
        "state_reason": "Persisted evidence counts support an observed quality review.",
        "input_count": 100,
        "output_count": 100,
        "budget_used": null,
        "evidence_actions": "Conflicts: 0",
        "recommendation": "",
        "fallback_action": "Quarantine weak evidence",
        "error_or_hard_stop": "",
        "kill_switch_state": "Available"
      },
      {
        "cell": "Policy & Masking",
        "release_availability": "Release 2",
        "activation_reason": "Mandatory before data leaves trust boundary",
        "duration_ms": null,
        "result": "Not fully evidenced",
        "state": "Insufficient Evidence",
        "state_reason": "No detailed policy/masking trace was persisted.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Fail closed; no direct fallback",
        "error_or_hard_stop": "",
        "kill_switch_state": "Emergency deny-all available"
      },
      {
        "cell": "Evidence & Trust",
        "release_availability": "Release 2",
        "activation_reason": "Every factual output package",
        "duration_ms": null,
        "result": "Continue",
        "state": "Observed",
        "state_reason": "Evidence trace and coverage are available.",
        "input_count": 100,
        "output_count": 100,
        "budget_used": null,
        "evidence_actions": "Mandatory coverage: Not measured",
        "recommendation": "Continue",
        "fallback_action": "Mark unverified; block when evidence floor is unmet",
        "error_or_hard_stop": "",
        "kill_switch_state": "Available"
      },
      {
        "cell": "Recovery & Resilience",
        "release_availability": "Release 2",
        "activation_reason": "No classified failure",
        "duration_ms": null,
        "result": "Not activated",
        "state": "Not Activated",
        "state_reason": "No classified failure required recovery for this run.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Certified fallback available by policy",
        "error_or_hard_stop": "",
        "kill_switch_state": "Force bypass available"
      },
      {
        "cell": "Data Acquisition Optimization",
        "release_availability": "P4",
        "activation_reason": "Optimize mode not active",
        "duration_ms": null,
        "result": "{'service_id': 'custom_st22_agent_service', 'entity_set': 'DumpHeader', 'system_id': 'PAL'}",
        "state": "Not Activated",
        "state_reason": "Optimize was not active or no route decision was required.",
        "input_count": 1,
        "output_count": 1,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Certified alternate route or direct safe path",
        "error_or_hard_stop": "",
        "kill_switch_state": "Source circuit breaker available"
      },
      {
        "cell": "MCP Tool Curation",
        "release_availability": "P4",
        "activation_reason": "Optimize mode not active",
        "duration_ms": null,
        "result": "Not activated",
        "state": "Not Activated",
        "state_reason": "Optimize was not active or no tool curation was required.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Certified direct safe set",
        "error_or_hard_stop": "",
        "kill_switch_state": "Tool curation can be disabled"
      },
      {
        "cell": "Retrieval Strategy Optimization",
        "release_availability": "P4",
        "activation_reason": "No retrieval optimization required",
        "duration_ms": null,
        "result": "Not activated",
        "state": "Not Activated",
        "state_reason": "No optimized retrieval strategy was recorded.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Exact or sparse retrieval, otherwise declare evidence gap",
        "error_or_hard_stop": "",
        "kill_switch_state": "Retrieval namespace can be disabled"
      },
      {
        "cell": "Vector Health and Routing",
        "release_availability": "P4",
        "activation_reason": "Vector path not selected",
        "duration_ms": null,
        "result": "Not activated",
        "state": "Not Activated",
        "state_reason": "Vector routing was not selected for this run.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "",
        "fallback_action": "Parent namespace or non-vector retrieval",
        "error_or_hard_stop": "",
        "kill_switch_state": "Vector namespace quarantine available"
      },
      {
        "cell": "Context Optimization",
        "release_availability": "P4",
        "activation_reason": "Optimize mode not active",
        "duration_ms": null,
        "result": "1629.0 bytes",
        "state": "Not Activated",
        "state_reason": "No optimized context package was recorded.",
        "input_count": 100,
        "output_count": 100,
        "budget_used": null,
        "evidence_actions": "Estimated compact tokens: 408",
        "recommendation": "",
        "fallback_action": "Compress optional content; preserve policy/evidence floor",
        "error_or_hard_stop": "",
        "kill_switch_state": "Certified context template available"
      },
      {
        "cell": "Performance and Cost Evaluation",
        "release_availability": "P5",
        "activation_reason": "Every controlled evaluation run",
        "duration_ms": 8450.429,
        "result": "8450.4 ms",
        "state": "Observed",
        "state_reason": "Run-level overhead was measured; cohort claims still require paired sample floors.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Aggregate only within the same pinned workload and cache-state cohort.",
        "fallback_action": "Retain local ledger when export is unavailable",
        "error_or_hard_stop": "",
        "kill_switch_state": "Metric export can be disabled without blocking execution"
      },
      {
        "cell": "Portfolio Economics",
        "release_availability": "P5",
        "activation_reason": "After paired functional and latency cohorts",
        "duration_ms": null,
        "result": "Awaiting 30/100 paired cohorts and named approval",
        "state": "Insufficient Evidence",
        "state_reason": "Release 2 can collect reuse and cost evidence, but enterprise-value claims require a signed G6 benchmark.",
        "input_count": null,
        "output_count": null,
        "budget_used": null,
        "evidence_actions": "",
        "recommendation": "Do not publish customer ROI or acceleration claims yet.",
        "fallback_action": "Keep the comparison evaluation-only",
        "error_or_hard_stop": "",
        "kill_switch_state": "Claim release gate enforced"
      }
    ],
    "show_relevant_cells_by_default": true,
    "p4_p5_runtime_activated": false,
    "release_gate": "P4/P5 controls are enabled only in Optimize mode. External acceleration claims still require paired sample floors, quality/evidence floors, rollback proof and named G6 approval.",
    "sap_evidence": {
      "applicable": false,
      "state": "Not Activated",
      "reason": "The selected run is not the Pre-Deployment Check Agent."
    }
  },
  "evidence_funnel": [
    {
      "stage": "Raw enterprise signals",
      "owner": "SAP / MCP / RAG / Vector",
      "records": 100,
      "bytes": 38899
    },
    {
      "stage": "Validated and authoritative",
      "owner": "EIA evidence contract",
      "records": 100,
      "coverage": {
        "count": 4,
        "authoritative": 2,
        "supporting": 2
      }
    },
    {
      "stage": "Deduplicated and correlated",
      "owner": "Deterministic evidence layer",
      "duplicates_removed": 0,
      "conflicts": 0
    },
    {
      "stage": "Compact model context",
      "owner": "Context boundary",
      "bytes": 1629,
      "estimated_tokens": 408
    },
    {
      "stage": "Interpretation and explanation",
      "owner": "LLM / Agent Hub",
      "final_owner": "Agent Hub"
    }
  ],
  "flow": [
    {
      "id": "intent",
      "label": "User intent",
      "owner": "Agent Hub",
      "changed": false,
      "detail": "Never changed by EIA"
    },
    {
      "id": "acquire",
      "label": "SAP / MCP / RAG / Vector signals",
      "owner": "Agent Hub",
      "changed": false,
      "detail": "Raw retrieval is not yet trusted evidence"
    },
    {
      "id": "validate",
      "label": "Validate authority & freshness",
      "owner": "EIA deterministic layer",
      "changed": true,
      "detail": "Schema, source, identity and evidence gates"
    },
    {
      "id": "reduce",
      "label": "Deduplicate & correlate",
      "owner": "EIA deterministic layer",
      "changed": true,
      "detail": "Remove noise and surface conflicts"
    },
    {
      "id": "compact",
      "label": "Compact business evidence",
      "owner": "EIA context boundary",
      "changed": true,
      "detail": "Only relevant verified evidence proceeds"
    },
    {
      "id": "reason",
      "label": "Interpret & explain",
      "owner": "LLM",
      "changed": false,
      "detail": "No raw enterprise truth ownership"
    },
    {
      "id": "result",
      "label": "Final response",
      "owner": "Agent Hub",
      "changed": true,
      "detail": "Agent Hub remains owner"
    }
  ]
}
```