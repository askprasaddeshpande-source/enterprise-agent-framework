# Minimum Authoritative Working Set — R2

## Objective

For mission `m`, minimize model-active context subject to enterprise correctness constraints.

Conceptually:

`min ModelActiveTokens(W)`

subject to:

- Mandatory Evidence Coverage = 100%
- Controlling Authority Coverage = 100%
- Required Conflict Coverage = 100%
- Required Policy/Approval Coverage = 100%
- Required Capability Coverage = 100%
- no silent invention of unknowns
- no silent suppression of blocking contradiction

## Candidate classes

- MANDATORY
- CONTROLLING_AUTHORITY
- SUPPORTING
- CONFLICTING
- REOBSERVATION_REQUIRED
- SUPERSEDED
- DUPLICATE
- STALE
- LOW_AUTHORITY
- MISSION_IRRELEVANT
- AUDIT_ONLY
- CAPABILITY_REQUIRED
- CAPABILITY_NOT_REQUIRED

## Reliability guard

Authority precedence is a policy ordering, not a guarantee of factual correctness.

When the strongest current authority is low-reliability and materially contradicts highly reliable, validated weaker evidence, MAWS does **not** silently let either side win. It emits `REOBSERVATION_REQUIRED`.

## Token rule

Token reduction counts as a successful EAF result only when frozen correctness gates are met.
