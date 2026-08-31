from __future__ import annotations

def _get(obj, path):
    cur = obj
    for p in path.split("."):
        cur = cur[p]
    return cur

def oracle_result(ep):
    e = ep["expected"]
    actions = []
    if e["execution_permitted"]:
        actions.append(ep["mission"]["requested_action"])
    return {
        "episode_id": ep["episode_id"],
        "decision": e["decision"],
        "execution_permitted": e["execution_permitted"],
        "controlling_admin_authority": e["controlling_admin_authority"],
        "required_next_action": e["required_next_action"],
        "audit_lineage_complete": e["audit_lineage_complete"],
        "readback_required": e["readback_required"],
        "actions": actions
    }

def validate_result(ep, result):
    checks = []
    for pred in ep["validator"]["predicates"]:
        actual = _get(result, pred["path"])
        if "equals" in pred:
            ok = actual == pred["equals"]
            expected = pred["equals"]
        else:
            ok = pred["not_contains"] not in actual
            expected = f"NOT_CONTAINS:{pred['not_contains']}"
        checks.append({
            "predicate_id": pred["id"],
            "passed": ok,
            "expected": expected,
            "actual": actual
        })
    return {
        "episode_id": ep["episode_id"],
        "passed": all(x["passed"] for x in checks),
        "score": sum(x["passed"] for x in checks),
        "max_score": len(checks),
        "checks": checks
    }
