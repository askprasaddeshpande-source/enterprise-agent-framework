from __future__ import annotations

def _get_path(obj, path):
    cur = obj
    for part in path.split("."):
        cur = cur[part]
    return cur

def validate_result(episode, result):
    checks = []
    for pred in episode["validator"]["predicates"]:
        actual = _get_path(result, pred["path"])
        if "equals" in pred:
            passed = actual == pred["equals"]
            expected = pred["equals"]
        elif "not_contains" in pred:
            passed = pred["not_contains"] not in actual
            expected = f"NOT_CONTAINS:{pred['not_contains']}"
        else:
            passed = False
            expected = "UNKNOWN_PREDICATE"
        checks.append({
            "predicate_id": pred["id"],
            "passed": passed,
            "expected": expected,
            "actual": actual,
        })
    return {
        "episode_id": episode["episode_id"],
        "passed": all(c["passed"] for c in checks),
        "score": sum(c["passed"] for c in checks),
        "max_score": len(checks),
        "checks": checks,
    }

def oracle_result(episode):
    e = episode["expected"]
    actions = []
    if e["execution_permitted"]:
        actions.append(episode["mission"]["action"])
    return {
        "episode_id": episode["episode_id"],
        "decision": e["decision"],
        "controlling_authority": e["controlling_authority"],
        "execution_permitted": e["execution_permitted"],
        "required_next_action": e["required_next_action"],
        "outcome_status": e["outcome_status"],
        "actions": actions,
    }
