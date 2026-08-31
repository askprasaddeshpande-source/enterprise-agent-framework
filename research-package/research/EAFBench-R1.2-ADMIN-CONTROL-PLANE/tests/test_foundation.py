from eafbench.generator import generate_dataset
from eafbench.validator import oracle_result, validate_result
from eafbench.metrics import compute_metrics, context_differential_metrics

def test_expected_dataset_size():
    rows = generate_dataset(20)
    assert len(rows) == 5 * 20 * 24

def test_differential_sets():
    rows = generate_dataset(20)
    assert len(set(r["differential_set_id"] for r in rows)) == 100

def test_oracle_passes_every_episode():
    rows = generate_dataset(2)
    for ep in rows:
        vr = validate_result(ep, oracle_result(ep))
        assert vr["passed"], (ep["episode_id"], vr)

def test_oracle_metrics_are_perfect():
    rows = generate_dataset(2)
    results = {ep["episode_id"]: oracle_result(ep) for ep in rows}
    m = compute_metrics(rows, results)
    dm = context_differential_metrics(rows, results)
    assert m["GTS"] == 1.0
    assert m["UAR"] == 0.0
    assert m["ARA"] == 1.0
    assert m["CER"] == 1.0
    assert m["PCR"] == 1.0
    assert dm["CSA"] == 1.0
    assert dm["CIR"] == 1.0
