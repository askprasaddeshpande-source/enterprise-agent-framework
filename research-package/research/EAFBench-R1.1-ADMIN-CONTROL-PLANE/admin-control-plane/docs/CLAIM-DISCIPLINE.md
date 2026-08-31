# Claim Discipline

This benchmark expands **architectural test coverage**. It does not raise the
observed operational evidence score by declaration.

Allowed before model evaluation:
- EAFBench now includes deterministic administration/control-plane cases.
- The benchmark contains explicit revocation, tenant isolation, delegation,
  approval, model/provider admission, tool admission, kill switch, audit, and
  readback scenarios.
- The benchmark is reproducible and model-independent at the ground-truth layer.

Not allowed before controlled evaluation:
- EAF prevents unauthorized actions better than a baseline.
- EAF improves security, compliance, quality, latency, cost, or ROI.
- EAF administration is production-proven across vendors.
