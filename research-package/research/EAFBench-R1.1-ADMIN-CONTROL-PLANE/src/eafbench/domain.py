from __future__ import annotations
import json
from .core import root_from_here

def load_domains():
    root = root_from_here()
    return json.loads((root / "config" / "domains.json").read_text(encoding="utf-8"))

def load_ontology():
    root = root_from_here()
    return json.loads((root / "config" / "ontology.json").read_text(encoding="utf-8"))

def load_splits():
    root = root_from_here()
    return json.loads((root / "config" / "splits.json").read_text(encoding="utf-8"))
