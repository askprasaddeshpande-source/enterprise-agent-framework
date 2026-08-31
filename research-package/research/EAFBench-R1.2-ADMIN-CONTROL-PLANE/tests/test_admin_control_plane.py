from eafadminbench.generator import generate_dataset
from eafadminbench.validator import oracle_result, validate_result
from eafadminbench.metrics import compute_metrics, differential_metrics

def test_admin_dataset_size():
    rows = generate_dataset(20)
    assert len(rows) == 5 * 20 * 20

def test_admin_differential_sets():
    rows = generate_dataset(20)
    assert len(set(r["admin_differential_set_id"] for r in rows)) == 100

def test_oracle_validates_all_admin_cases():
    rows = generate_dataset(2)
    for ep in rows:
        v = validate_result(ep, oracle_result(ep))
        assert v["passed"], (ep["episode_id"], v)

def test_admin_oracle_metrics_are_perfect():
    rows = generate_dataset(2)
    results = {ep["episode_id"]: oracle_result(ep) for ep in rows}
    m = compute_metrics(rows, results)
    d = differential_metrics(rows, results)
    assert m["ADMIN_GTS"] == 1.0
    assert m["ADMIN_UAR"] == 0.0
    for k in ("ARI","TIR","PPA","RER","DBA","ABA","KSE","MPC","TAA","ALC","ORA"):
        assert m[k] == 1.0, (k, m[k])
    assert d["ASA"] == 1.0
    assert d["AIR"] == 1.0

def test_revocation_and_kill_switch_forbid_action():
    rows = generate_dataset(1)
    targets = [e for e in rows if e["scenario_family"] in {
        "A06_CAPABILITY_REVOKED", "A11_KILL_SWITCH_ACTIVE", "A19_REVOCATION_PROPAGATION"
    }]
    assert targets
    for ep in targets:
        assert ep["expected"]["execution_permitted"] is False
        assert ep["mission"]["requested_action"] in ep["expected"]["forbidden_actions"]
