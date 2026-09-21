# Research directions

The survey uses seven directions to make unlike tasks comparable. They are **evaluation lenses, not mutually exclusive boxes**: for example, an HLS agent may also be a repository-scale system, while a PCB benchmark may test either question answering or interactive routing. Cross-cutting terms follow [`docs/taxonomy.md`](../../docs/taxonomy.md).

## 1. Task contract

| Direction | Research question | Typical input | Expected output | Typical interaction |
|---|---|---|---|---|
| RTL generation | Can a model translate a bounded specification or partial design into functionally correct HDL? | Natural-language specification, module interface, or partial Verilog | Verilog/SystemVerilog module | Usually single-shot generation; the evaluator runs tools afterward |
| Formal verification | Can a model express intended behavior as valid, meaningful formal properties? | Property description plus testbench context, or design RTL alone | SystemVerilog Assertions and supporting formal-testbench code | Usually single-shot generation; the evaluator invokes the formal tool |
| Repository-scale RTL | Can a model or agent use project-scale context to complete, reason about, or repair RTL? | Partial design or issue description plus repository context; agents may also receive a build environment and tests | RTL completion, reasoning answer, or one-/multi-file patch | Ranges from single-shot repository-conditioned generation to long-horizon search, editing, and test feedback |
| HLS and co-design | Can AI produce synthesizable accelerator code and, in broader tasks, coordinate it with software and a system? | Specification or existing C/C++ plus HLS/system context | HLS C/C++, directives, and sometimes integration code | Published baselines range from single-shot HLS generation to tool-using integration agents |
| Physical-design agents | Can an agent advance a design through synthesis and physical implementation while responding to EDA state? | RTL, constraints, technology setup, reports, and tool state | Scripts/actions plus netlist, layout, reports, or ECO results | Long-horizon, tool-interactive execution |
| Analog and SPICE | Can AI preserve circuit structure or meet electrical goals in simulator-facing circuit workflows? | Circuit requirements or an existing SPICE netlist | Answer, edited netlist, topology, or parameters | Mixed: single-shot structural tasks and simulator-in-the-loop optimization/repair |
| Schematic and PCB | Can AI understand, generate, or modify native board artifacts under engineering checks? | Requirements, schematic/board files, connectivity, placement, and rules | Answer, schematic, layout, or routing actions | Mixed: single-shot QA/generation and interactive routing agents |

The interaction column describes the **evaluated system**. A compiler, simulator, formal tool, or DRC engine used only by the scorer does not turn a single-shot model into a tool-using agent.

## 2. Evidence contract

| Direction | Strongest common oracle and metrics | Representative benchmark / method shape |
|---|---|---|
| RTL generation | Compilation plus functional simulation; pass@k or pass rate | [VerilogEval](../benchmarks/verilog-eval.md); prompted or fine-tuned code-generation models |
| Formal verification | SVA syntax, formal equivalence/implication, or proof results; exact/partial functional accuracy and pass@k | [FVEval](../benchmarks/fveval.md); natural-language-to-SVA and design-to-SVA models |
| Repository-scale RTL | Textual or formal scoring for completion/reasoning, or fail-to-pass project verification for repair; task accuracy or resolved-task rate | RTL-Repo and RTL-BenchLS for single-shot repository-conditioned tasks; [HWE-Bench-Repair](../benchmarks/hwe-bench-repair.md) for coding agents with repository and shell access |
| HLS and co-design | C compilation/simulation, HLS synthesis, and sometimes deployment; stage pass rates, pass@k, or QoR | [HLS-Eval](../benchmarks/hls-eval.md); HLS generators/editors and integration agents |
| Physical-design agents | Executed EDA stages and physical metrics; completion, timing/area/power score, runtime, and cost | [RTL-to-GDS agent case study](../benchmarks/fluxbench.md) (local catalog id `fluxbench`); general coding agents and structured EDA agents |
| Analog and SPICE | Structural equivalence or SPICE simulation; task accuracy or specification success under a budget | [NetlistBench](../benchmarks/netlistbench.md); single-shot netlist manipulation (simulator-guided methods test a different claim) |
| Schematic and PCB | Answer checks, ERC/DRC, connectivity, and engine-derived routing metrics | [PCBWorld](../benchmarks/pcbworld.md); RL, tool-calling LLM, and rule-based routing agents |

## 3. Claim boundary and maturity

| Direction | Evidence can support | Evidence does **not** by itself support | Working maturity and largest gap |
|---|---|---|---|
| RTL generation | Functional behavior on isolated, testbench-covered modules | Repository integration, exhaustive correctness, or competitive physical quality | Most established benchmark family; hidden-test breadth and contamination controls remain uneven |
| Formal verification | Syntactic validity and formally checked relationships for generated properties | Complete production-design coverage or autonomous formal-tool operation | Strong oracle on bounded tasks; public-tool portability and usefulness/coverage metrics lag |
| Repository-scale RTL | Repository-conditioned completion/reasoning or repair under the benchmark's stated scorer | Correctness beyond that textual, formal, or regression contract; general hardware-product engineering | Growing realistic task family; oracle strength varies, while leakage and environment longevity remain risks |
| HLS and co-design | Functional and synthesizable HLS code, or integration in the specifically executed system | Physical closure, portability across HLS vendors, or deployment unless explicitly run | HLS generation has executable stages; end-to-end hardware/software co-design remains early |
| Physical-design agents | Ability to operate a specified flow and produce measured implementation artifacts | A model-only ranking or generalization across designs, PDKs, tool versions, and budgets | Emerging; current representative evidence is a single-design commercial-flow case study |
| Analog and SPICE | Exact netlist-structure preservation or simulated electrical behavior, depending on the benchmark | Structural correctness implying electrical performance, or simulation implying layout/signoff readiness | Fragmented between structure, sizing, and repair; shared multi-stage evaluation is missing |
| Schematic and PCB | Board understanding or engine-checked routing under the represented rules | Intended electrical function, component suitability, manufacturability, or firmware integration | Interactive routing is now executable; coordinated schematic–PCB–BOM–firmware change remains weakly measured |

“Mature” here means that task contracts and executable evaluators are comparatively established. It does not mean that AI systems are ready for unsupervised production use.

## 4. Evidence status and remaining work

Each linked worked card has been checked against its primary paper and, where located, the official release. `source-checked` means the stated task contract and availability were checked; it does **not** mean every reported model result has been independently reproduced.

Before a direction becomes a manuscript section, it still needs:

1. An original task/evaluation diagram.
2. A multi-benchmark comparison with input, output, scale, interaction, oracle, and availability.
3. A method-family comparison explaining representative systems.
4. Cross-checked findings with explicit limitations.
5. A section thesis, final table, final figure, and open-problem callout.

The 22-row catalog remains a discovery index. This direction-level synthesis should not be read as a completed row-by-row audit.
