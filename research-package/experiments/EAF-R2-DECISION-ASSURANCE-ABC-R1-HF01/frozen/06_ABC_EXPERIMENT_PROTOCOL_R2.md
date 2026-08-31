# R2 A/B/C Experimental Protocol

## Arm A — Native

Raw enterprise evidence → same model → proposal → symbolic environment.

Purpose: native model behavior under noisy enterprise context.

## Arm B — Governance

Raw enterprise evidence + deterministic authority/admin governance envelope → same model → external enforcement → symbolic environment.

Purpose: isolate governance/safety effect.

## Arm C — Full EAF

Raw evidence → authority/temporal/reliability resolution → evidence sufficiency → MAWS → same model → deterministic enforcement → symbolic environment → authoritative readback gate.

Purpose: test combined assurance + context/noise reduction + outcome validation.

## Comparisons

- A→B: governance/control effect
- B→C: context/evidence assurance effect
- A→C: total EAF effect

## Fixed runtime defaults

- provider: local Ollama
- model: `qwen3:8b`
- temperature: 0
- seed: 20260829
- num_ctx: 8192
- num_predict: 1200
- think: false
- stream: false
- keep_alive: 30m
- timeout: 600 s
- concurrency: 1
- provider retries: 0

The actual local model digest, Ollama server version and model-show hash are captured and frozen by `prepare` before any scientific call.
