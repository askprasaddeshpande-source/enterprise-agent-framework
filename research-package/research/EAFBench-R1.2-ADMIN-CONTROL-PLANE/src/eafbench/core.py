from __future__ import annotations
import hashlib, json
from pathlib import Path

def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_obj(obj) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()

def stable_int(*parts: str) -> int:
    raw = "|".join(parts).encode("utf-8")
    return int(hashlib.sha256(raw).hexdigest()[:16], 16)

def root_from_here() -> Path:
    return Path(__file__).resolve().parents[2]
