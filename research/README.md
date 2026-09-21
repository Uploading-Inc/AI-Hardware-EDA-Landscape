# Research library

This directory is the evidence layer behind the survey. It is organized for writing a paper, not for collecting links.

If you are new to the field, read the [field guide](../docs/field-guide.md) first. This directory is the next layer down: it shows how each benchmark or method supports—or fails to support—a survey claim.

## From paper discovery to manuscript

```mermaid
flowchart LR
    A[Discover paper] --> B[Verify primary sources]
    B --> C[Create benchmark or method card]
    C --> D[Place in a research direction]
    D --> E[Compare within direction]
    E --> F[Synthesize across directions]
    F --> G[Write paper section]
    G --> H[Generate tables and original figures]
```

Each claim in the final manuscript should be traceable backwards through this chain. A paper title in a reading list is not sufficient evidence.

## Research units

### Benchmark card

A benchmark card describes exactly what is evaluated:

- task and motivation;
- input and expected output;
- evaluation unit and dataset provenance;
- model or agent interaction regime;
- tool environment and success oracle;
- metrics, baselines, and headline results;
- reproducibility status and limitations;
- claim-level evidence and primary links;
- an original pipeline diagram suitable for later redrawing as a paper figure.

See [`templates/benchmark-card.md`](templates/benchmark-card.md).

### Method card

A method card describes how a proposed system works:

- problem addressed and core idea;
- architecture, stages, and feedback loops;
- training and inference setup;
- tools, models, and external dependencies;
- benchmarks used and comparison baselines;
- reported gains, ablations, and limitations;
- an original method diagram derived from the paper.

See [`templates/method-card.md`](templates/method-card.md).

### Direction brief

A direction brief becomes the evidence scaffold for one survey section. It defines the area, explains its evolution, compares benchmarks and methods, identifies recurring evaluation practices, and records unresolved disagreements or gaps.

See [`templates/direction-brief.md`](templates/direction-brief.md) and the current [direction map](directions/README.md).

## Verification states

| State | Meaning | May support a manuscript claim? |
|---|---|---:|
| `seed` | Discovered in an initial search; metadata or interpretation may still change | No |
| `source-checked` | Paper and official artifacts inspected; factual fields extracted | With caution |
| `cross-checked` | Important claims checked across paper, code/data, and venue records | Yes |
| `frozen` | Included in the manuscript evidence snapshot | Yes |

Cards must state their status and last verification date. Missing information should be written as `not located`, not silently inferred.

## Figure policy

- Do not copy a paper's figure into this repository unless its license and attribution explicitly permit reuse.
- Prefer original Mermaid sketches during research.
- Before publication, redraw final figures from verified facts using a consistent visual system.
- Every figure must have a short evidence note identifying which papers support each component.
- A conceptual synthesis figure must be labeled as our interpretation rather than a figure from the cited work.

## Current contents

The first pass includes one worked benchmark card for each major direction. These cards demonstrate the required depth; they do not imply that the remaining catalog entries have already been fully audited.

| Direction | Worked example |
|---|---|
| RTL generation | [VerilogEval](benchmarks/verilog-eval.md) |
| Formal verification | [FVEval](benchmarks/fveval.md) |
| Repository-scale repair | [HWE-Bench-Repair](benchmarks/hwe-bench-repair.md) |
| HLS and co-design | [HLS-Eval](benchmarks/hls-eval.md) |
| Physical design agents | [RTL-to-GDS agent case study](benchmarks/fluxbench.md) |
| Analog and SPICE | [NetlistBench](benchmarks/netlistbench.md) |
| Schematic and PCB | [PCBWorld](benchmarks/pcbworld.md) |
