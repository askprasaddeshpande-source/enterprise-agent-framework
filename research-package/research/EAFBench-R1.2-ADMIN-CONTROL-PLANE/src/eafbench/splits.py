from __future__ import annotations
from .domain import load_splits

def split_for_family(family: str) -> str:
    cfg = load_splits()
    for split_name in ("HELD_OUT", "ADVERSARIAL", "FALSIFICATION", "VALIDATION"):
        if family in cfg[split_name]:
            return split_name
    return "DEVELOPMENT"
