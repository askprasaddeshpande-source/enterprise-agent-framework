from __future__ import annotations
import argparse, json
from pathlib import Path

def treatment_packet(episode):
    # This is a research harness packet, not an EAF implementation.
    return {
        "episode_id": episode["episode_id"],
        "arm": "TREATMENT_B_EAF",
        "mission": episode["mission"],
        "observations": episode["agent_observation"],
        "required_controls": [
            "PROVENANCE_VALIDATION",
            "AUTHORITY_RESOLUTION",
            "TEMPORAL_RESOLUTION",
            "EVIDENCE_SUFFICIENCY",
            "POLICY_EVALUATION",
            "CAPABILITY_AUTHORIZATION",
            "APPROVAL_EVALUATION",
            "EXECUTION_GOVERNANCE",
            "READBACK_VALIDATION"
        ],
        "ground_truth_exposed": False,
    }

def control_packet(episode):
    return {
        "episode_id": episode["episode_id"],
        "arm": "CONTROL_A",
        "mission": episode["mission"],
        "observations": episode["agent_observation"],
        "ground_truth_exposed": False,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    with open(args.dataset, encoding="utf-8") as f:
        rows = [json.loads(line) for _, line in zip(range(args.limit), f)]
    for ep in rows:
        eid = ep["episode_id"]
        (out / f"{eid}.control.json").write_text(json.dumps(control_packet(ep), indent=2), encoding="utf-8")
        (out / f"{eid}.treatment.json").write_text(json.dumps(treatment_packet(ep), indent=2), encoding="utf-8")
    print(json.dumps({"episodes_prepared": len(rows), "model_calls": 0, "output": str(out)}, indent=2))

if __name__ == "__main__":
    main()
