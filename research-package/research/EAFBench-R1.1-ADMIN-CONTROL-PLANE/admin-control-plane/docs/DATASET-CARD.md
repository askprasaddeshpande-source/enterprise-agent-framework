# EAFBench R1.1 — Administration & Control Plane Dataset Card

## Scope

This benchmark evaluates EAF as an **enterprise agent administration and runtime
control plane**. It does not test only natural-language quality.

## Size

- Canonical administrative missions: **100**
- Differential sets: **100**
- Administrative variants per mission: **20**
- Executable episodes: **2000**
- Domains: **5**
- Model calls used to generate canonical truth: **0**

## Administrative differential families

- `A01_REGISTERED_VALID` — Registered, enabled, same-tenant agent with current policy and valid grants.
- `A02_UNREGISTERED_AGENT` — Agent exists technically but is absent from the enterprise agent registry.
- `A03_DISABLED_AGENT` — Registered agent has been administratively disabled.
- `A04_TENANT_SCOPE_VIOLATION` — Agent attempts to act outside its registered tenant scope.
- `A05_POLICY_VERSION_CHANGE` — A newer active policy changes the runtime decision relative to a prior policy.
- `A06_CAPABILITY_REVOKED` — Capability was previously granted but is now revoked.
- `A07_DELEGATION_WITHIN_SCOPE` — Delegation narrows or preserves scope and remains valid.
- `A08_DELEGATION_SCOPE_ESCALATION` — Agent attempts to delegate authority it does not possess.
- `A09_APPROVAL_MISSING` — Consequential action requires approval but no valid approval exists.
- `A10_APPROVAL_REVOKED` — Previously valid approval is revoked before execution.
- `A11_KILL_SWITCH_ACTIVE` — Emergency administrative kill switch overrides otherwise valid permission.
- `A12_MODEL_PROVIDER_NOT_ALLOWED` — Requested model/provider is outside the registered policy allowlist.
- `A13_TOOL_MCP_NOT_ADMITTED` — Tool/MCP capability is discoverable but not admitted for this agent/tenant.
- `A14_SHARED_POLICY_REUSE` — A shared policy is applied consistently across multiple registered agents.
- `A15_RETIRED_AGENT` — Retired agent retains technical reachability but must not execute.
- `A16_AUDIT_LINEAGE_MISSING` — Execution request lacks required policy/authority lineage evidence.
- `A17_READBACK_MISMATCH` — Action transport reports success but authoritative final state does not match.
- `A18_ADMIN_POLICY_CONFLICT` — Two active administrative policies conflict at equal administrative precedence.
- `A19_REVOCATION_PROPAGATION` — Revoked capability must be denied across all agents that inherited the shared grant.
- `A20_EMERGENCY_OVERRIDE` — Explicit scoped emergency override permits a normally blocked action and must be separately traceable.

## Primary benchmark question

Does a governed runtime change its decision correctly when **administrative
authority changes**, while remaining stable when an administrative variation
should not change the outcome?

## Differential metrics

- **ASA — Administrative Sensitivity Accuracy:** correct decision transition
  when material administrative state changes.
- **AIR — Administrative Invariance Rate:** correct decision stability when
  administrative variation does not require a different outcome.

## Control-plane metrics

- **ARI** Agent Registration Integrity
- **TIR** Tenant Isolation Rate
- **PPA** Policy Propagation Accuracy
- **RER** Revocation Enforcement Rate
- **DBA** Delegation Boundary Accuracy
- **ABA** Approval Boundary Accuracy
- **KSE** Kill Switch Effectiveness
- **MPC** Model/Provider Policy Compliance
- **TAA** Tool Admission Accuracy
- **ALC** Audit Lineage Correctness
- **ORA** Outcome Readback Accuracy

These metric names are operational definitions for this benchmark. Oracle scores
measure benchmark consistency only.
