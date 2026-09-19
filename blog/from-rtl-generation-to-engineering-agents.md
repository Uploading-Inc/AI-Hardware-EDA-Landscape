# From RTL Generation to Engineering Agents: What Hardware Benchmarks Actually Measure

*Working draft · 19 September 2026*

The first wave of language-model benchmarks for hardware design asked an important but narrow question: can a model turn a natural-language specification into Verilog that passes a testbench?

That question is no longer enough.

Recent evaluation has moved outward in several directions at once. Formal-verification benchmarks test whether a model can produce properties that prove or expose real behavior. Repository benchmarks ask it to locate faults across large projects. Physical-design and PCB environments require it to operate engineering tools. Analog benchmarks close the loop through simulation. Hardware–software co-design tasks demand coordination across compilation, integration, and deployment.

The result is a crowded landscape in which two benchmarks can both be described as “hardware evaluation” while measuring almost entirely different capabilities. The right organizing question is therefore not just *which design stage is covered?* It is *what engineering work must the system perform, and what evidence determines success?*

## The five axes hiding inside “hardware benchmark”

Five dimensions separate a toy generation task from an engineering benchmark.

First is **context scale**. A self-contained RTL problem tests local synthesis from a specification. A repository repair task also tests search, dependency discovery, fault localization, and the ability to avoid collateral damage.

Second is **interaction**. A model whose output is later compiled by an evaluator is still a single-shot generator. An agent becomes meaningfully tool-using only when compiler, simulator, formal, or EDA feedback can change its next action.

Third is **oracle strength**. Text similarity is convenient but weak for artifacts with many equivalent implementations. Compilation rules out malformed output. Simulation tests selected behaviors. Formal methods can establish stronger properties within a stated model. Physical checks and deployment cover constraints that source-level evaluation misses.

Fourth is **artifact breadth**. Many benchmarks stop at one HDL file. Real engineering changes may span RTL, assertions, configuration, build logic, firmware, schematics, layouts, and component constraints.

Fifth is **engineering realism**. Synthetic problems are valuable because they are controlled and inexpensive. Historical issues and native tool environments are valuable because they contain the inconvenient dependencies, ambiguous requirements, and failure modes that controlled problems omit.

## Four generations of evaluation

The literature can be read as four overlapping regimes rather than a clean chronological replacement.

### 1. Generation-centric benchmarks

VerilogEval and RTLLM established the modern baseline: convert a specification into RTL and execute it against tests. Their lasting contribution is not that they solved hardware design, but that they made functional execution the norm for evaluating generated HDL.

### 2. Verification-grounded benchmarks

FVEval and the AssertLLM line elevate verification itself into the task. HLS-Eval separates parseability, compilation, execution, and synthesis instead of collapsing them into one score. AnalogGym and simulation-driven analog systems show the same principle in a different domain: plausible text is not an engineering result.

### 3. Repository- and system-scale benchmarks

RTL-Repo introduced repository-conditioned completion, but its textual oracle also illustrates the limits of repository context without functional validation. Newer repair benchmarks reconstruct historical issues and run native regressions. Hardware–software co-design benchmarks expand the unit of work again, from a patch to an integrated system.

### 4. Environment-grounded agents

ChatEDA, physical-design agent benchmarks, PCBWorld, and simulation-guided SPICE agents treat the engineering environment as part of the benchmark. These systems must decide what to inspect, which tool to invoke, how to interpret failures, and when to revise a design. At this point, evaluating only the foundation model is misleading: the scaffold, tool interface, budget, and environment matter too.

## The missing benchmark is not another isolated task

The clearest gap lies at board and product level. Existing work separately covers component-aware schematic generation, PCB understanding, native routing, repository repair, and hardware–software integration. What remains largely unmeasured is a realistic engineering-change request that couples them.

Imagine a task that begins with an existing open hardware repository and asks an agent to add a sensor. Success might require selecting a part from datasheets, changing the schematic and PCB, updating the BOM, modifying firmware and drivers, running electrical and design-rule checks, building the firmware, and demonstrating the requested behavior in a simulator or test fixture. Every individual step has an analogue in current research, but the coordinated task does not yet have a mature, widely adopted benchmark.

This gap matters because local validity is not functional intent. A schematic can pass electrical rules while connecting the wrong signal. A board can pass DRC while violating a placement constraint. Firmware can compile while targeting a stale pin map. The challenge is not merely to generate valid artifacts; it is to preserve intent across representations.

## What future benchmark reports should disclose

As tasks become agentic, benchmark papers need a stronger experimental contract. At minimum they should report:

- the exact model and agent scaffold;
- prompts, tools, permissions, and environment versions;
- token, tool-call, simulator, and wall-clock budgets;
- task provenance and contamination controls;
- the sequence of oracles used to determine success;
- failure categories, not only aggregate pass rates;
- the cost and reproducibility limits of commercial tools;
- which artifacts are public and which require reconstruction.

Hardware engineering is unusually well suited to executable evaluation, but only if benchmark designers resist the temptation to compress every stage into one headline score.

## Where this project goes next

This repository will audit the emerging benchmark landscape paper by paper, encode it in a machine-readable catalog, and use the result to develop a survey centered on capability, interaction, and evidence. The immediate goal is not to declare a winner. It is to make benchmark claims comparable enough that researchers can tell what progress actually means.

## Selected primary sources

- [VerilogEval: Evaluating Large Language Models for Verilog Code Generation](https://arxiv.org/abs/2309.07544)
- [FVEval: Understanding Language Model Capabilities in Formal Verification of Digital Hardware](https://arxiv.org/abs/2410.23299)
- [HLS-Eval: A Benchmark and Framework for Evaluating LLMs on High-Level Synthesis Design Tasks](https://arxiv.org/abs/2504.12268)
- [HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks](https://arxiv.org/abs/2604.14709)
- [RTL-BenchLS: A Large-Scale Benchmark for RTL Reasoning and Generation with Large Language Models](https://arxiv.org/abs/2606.08976)
- [HSCO-Bench: An Agent-Driven End-to-End Hardware-Software Co-design Benchmark for Systems-on-Chip](https://arxiv.org/abs/2605.19399)
- [PDAGENT-BENCH: Characterizing, Grounding, and Architecting LLM Agents for VLSI Physical Design](https://arxiv.org/abs/2606.17253)
- [PCB-QA: Evaluating LLMs over the First Printed Circuit Board Design Question-Answer Dataset](https://arxiv.org/abs/2606.23704)
- [PCBWorld: A Benchmark Environment for Engine-Grounded PCB Design Automation](https://arxiv.org/abs/2607.05915)
- [FluxBench: Can AI Agents Really Complete RTL-to-GDS?](https://arxiv.org/abs/2607.17528)

The full seed bibliography and release links are maintained in [`data/benchmarks.csv`](../data/benchmarks.csv). Quantitative claims will be added to the essay only after row-level verification.
