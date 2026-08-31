from __future__ import annotations
import argparse, json
from pathlib import Path
from .generator import generate_dataset
from .core import root_from_here

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--missions-per-domain", type=int, default=20)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    root = root_from_here()
    out = Path(args.out) if args.out else root / "admin-control-plane" / "dataset" / "eaf-admin-bench-v1.1.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = generate_dataset(args.missions_per_domain)
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    print(json.dumps({"episodes": len(rows), "model_calls": 0, "output": str(out)}, indent=2))

if __name__ == "__main__":
    main()
