from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict

def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    rows = load_jsonl(args.dataset)
    by_split = Counter(r["split"] for r in rows)
    by_domain = Counter(r["domain"] for r in rows)
    by_family = Counter(r["scenario_family"] for r in rows)
    by_decision = Counter(r["expected"]["decision"] for r in rows)
    diff_sets = len(set(r["differential_set_id"] for r in rows))

    report = {
        "dataset": args.dataset,
        "episodes": len(rows),
        "differential_sets": diff_sets,
        "splits": dict(sorted(by_split.items())),
        "domains": dict(sorted(by_domain.items())),
        "families": dict(sorted(by_family.items())),
        "expected_decisions": dict(sorted(by_decision.items())),
        "model_calls": 0,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, sort_keys=True)
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
