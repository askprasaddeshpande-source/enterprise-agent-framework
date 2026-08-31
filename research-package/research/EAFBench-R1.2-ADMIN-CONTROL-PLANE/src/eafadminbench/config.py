from __future__ import annotations
import json
from .core import root_from_here

def _load(name):
    p = root_from_here() / "admin-control-plane" / "config" / name
    return json.loads(p.read_text(encoding="utf-8"))

def domains():
    return _load("domains.json")

def ontology():
    return _load("ontology.json")

def splits():
    return _load("splits.json")

def split_for_family(family):
    s = splits()
    for name in ("HELD_OUT", "ADVERSARIAL", "FALSIFICATION", "VALIDATION"):
        if family in s[name]:
            return name
    return "DEVELOPMENT"
