from __future__ import annotations
import hashlib, json
from pathlib import Path

def root_from_here() -> Path:
    return Path(__file__).resolve().parents[2]

def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_obj(obj):
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()

def stable_int(*parts):
    return int(hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:16], 16)
