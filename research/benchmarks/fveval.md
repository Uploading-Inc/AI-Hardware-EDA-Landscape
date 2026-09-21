# FVEval

| Field | Value |
|---|---|
| Research direction | Formal verification |
| Paper | [FVEval: Understanding Language Model Capabilities in Formal Verification of Digital Hardware](https://arxiv.org/abs/2410.23299) |
| Official artifacts | [NVlabs/FVEval](https://github.com/NVlabs/FVEval) |
| First public year / venue | 2024 preprint / DATE 2025 |
| Verification status | `source-checked` for task families, scale, oracles, and tool requirements; model-result audit pending |
| Last checked | 2026-09-21 |

## One-sentence definition

FVEval measures language-model capability on progressively harder formal-verification tasks centered on generating SystemVerilog Assertions.

## Why it exists

Passing an RTL testbench does not show whether a model can express design intent as formal properties. FVEval treats verification collateral itself as the generated artifact and evaluates it with a formal tool.

## Benchmark anatomy

| Component | Description |
|---|---|
| Evaluation unit | One natural-language-to-SVA or design-to-SVA verification task |
| Input | Natural-language property descriptions, testbench/design context, or RTL depending on sub-benchmark |
| Expected output | SystemVerilog Assertions, with accompanying formal-testbench code where needed |
| Dataset source | Expert-written collateral plus scalable synthetic examples aligned with formal-verification workflows |
| Scale | 79 NL2SVA-Human assertions, 300 NL2SVA-Machine cases, and 192 Design2SVA designs (96 pipelines and 96 FSMs) |
| Interaction | Canonically single-shot model evaluation; the evaluator invokes formal tools externally |
| Environment | Cadence Jasper, as required by the released evaluation flow |
| Success oracle | Jasper syntax checks; formal equivalence for exact NL2SVA correctness, one-way formal implication for partial correctness, and proof outcomes for Design2SVA |
| Metrics | Syntax accuracy, exact functional accuracy by equivalence, partial functional accuracy by implication, BLEU as a reported non-oracle comparison, and pass@k where multiple samples are evaluated |

## Evaluation pipeline

```mermaid
flowchart LR
    A[Natural language plus design context] --> B[Language model]
    B --> C[Generated SVA]
    C --> D[Parse and elaborate]
    D --> E[Formal verification in Jasper]
    E --> F[Validity and functional correctness]
```

## What it demonstrates

- Whether a model can translate design intent into formally checkable assertions.
- How performance changes as the input moves from directed natural-language properties toward design-level reasoning.

## What it does not demonstrate

- That the evaluated model autonomously operates the formal tool; in the canonical setup, tool execution belongs to the evaluator.
- Complete verification coverage of a production design.

## Reproducibility

| Artifact | Availability | Notes |
|---|---|---|
| Paper | Yes | Public preprint and DATE record |
| Dataset | Yes | Released in the official repository |
| Evaluator | Yes | Scripts and task data are public |
| Environment | Commercial | Full evaluation requires Cadence Jasper access |

## Open questions

- Which results can be reproduced without the commercial formal tool?
- How should assertion usefulness be compared across syntax, provability, coverage, and bug-finding power?
