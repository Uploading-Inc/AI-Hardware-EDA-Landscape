# NetlistBench

| Field | Value |
|---|---|
| Research direction | Analog and SPICE netlist manipulation |
| Paper | [NetlistBench: Evaluating LLM Reliability in SPICE Netlist Recognition and Manipulation](https://arxiv.org/abs/2608.12197) |
| Official artifacts | Public repository not located in the initial source pass |
| First public year / venue | 2026 / arXiv |
| Verification status | `source-checked` for task taxonomy, scale, and oracle; artifact audit pending |
| Last checked | 2026-09-19 |

## One-sentence definition

NetlistBench isolates whether language models can recognize and manipulate the structured topology and parameters encoded in textual SPICE netlists.

## Why it exists

An LLM may produce plausible circuit text while silently corrupting connectivity, hierarchy, or device parameters. Higher-level analog-design scores can hide this low-level structural failure mode.

## Benchmark anatomy

| Component | Description |
|---|---|
| Evaluation unit | One recognition, edit, equivalence, or compound netlist task |
| Input | A SPICE netlist plus a question or edit instruction |
| Expected output | An answer or modified SPICE netlist |
| Dataset source | Constructed cases spanning local and hierarchical structural operations |
| Scale | 2,342 cases across 24 task families |
| Interaction | Single-shot or reasoning-model response in the reported evaluation |
| Environment | Structure-aware parser/evaluator rather than a full analog design loop |
| Success oracle | Deterministic comparison of netlist structure, connectivity, parameters, or equivalence target |
| Metrics | Accuracy by task family, complexity, reasoning setting, and edit horizon |

## Evaluation pipeline

```mermaid
flowchart LR
    A[SPICE netlist plus instruction] --> B[Language model]
    B --> C[Answer or edited netlist]
    C --> D[Parse circuit structure]
    D --> E[Deterministic structural oracle]
    E --> F[Accuracy by operation family]
```

## What it demonstrates

- Whether a model preserves simulator-facing circuit structure during targeted manipulation.
- How reliability changes with operation complexity and longer edit horizons.

## What it does not demonstrate

- That an edited circuit meets analog performance specifications under SPICE simulation.
- Layout, parasitics, PPA closure, or a complete analog design methodology.

## Reproducibility

| Artifact | Availability | Notes |
|---|---|---|
| Paper | Yes | Public preprint |
| Dataset | Not located | Recheck before manuscript freeze |
| Evaluator | Not located | Deterministic oracle is described in the paper |
| Environment | Unclear | Full release status requires verification |

## Open questions

- Will the structural oracle and data generator be released in a reusable form?
- How well do structural results predict success in simulator-grounded repair tasks?
