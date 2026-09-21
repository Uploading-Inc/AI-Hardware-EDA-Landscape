# Glossary

This glossary defines the hardware-design and evaluation terms used throughout the survey. Definitions are intentionally practical: they explain how a term affects the task or benchmark, rather than attempting to replace a hardware-design textbook.

## Hardware-design flow

| Term | Plain-language meaning | Why it matters in this survey |
|---|---|---|
| **EDA** | Electronic design automation: software used to design, verify, and implement electronic hardware. | An “EDA agent” acts through tools rather than only returning text. |
| **HDL** | Hardware description language, such as Verilog or VHDL. | It describes hardware structure and behavior, not an ordinary sequential program. |
| **RTL** | Register-transfer level: a clock- and register-oriented description of digital logic, commonly written in Verilog or SystemVerilog. | Many early benchmarks ask a model to generate one isolated RTL module. |
| **HLS** | High-level synthesis: conversion of C/C++ or another higher-level description into RTL. | HLS benchmarks must check both software-like correctness and hardware synthesizability. |
| **Synthesis** | Translation of RTL into a technology-oriented gate-level representation. | Successful simulation does not guarantee successful synthesis or good implementation quality. |
| **Netlist** | A structured list of components or logic cells and the connections between them. | Digital and analog netlists require connectivity-preserving edits that text similarity may miss. |
| **Physical design** | Transformation of a logical circuit into a geometric chip implementation. | Agents may need to operate placement, routing, timing, and optimization tools. |
| **Place and route (P&R)** | Placement of circuit elements followed by routing of their physical connections. | P&R results are evaluated with physical and quality-of-results checks. |
| **ECO** | Engineering change order: a targeted late-stage design modification. | It tests whether an agent can repair a design without rerunning or disrupting everything. |
| **ASIC** | Application-specific integrated circuit: a chip manufactured for a particular purpose. | ASIC results depend on technology libraries, tools, and implementation constraints. |
| **FPGA** | Field-programmable gate array: reconfigurable hardware that can implement a digital design. | FPGA deployment can provide stronger system evidence than source-level tests alone. |
| **SoC** | System on chip: a system combining processors, accelerators, memory, interfaces, and other blocks. | SoC tasks expose hardware–software integration and cross-component dependencies. |

## Circuits and boards

| Term | Plain-language meaning | Why it matters in this survey |
|---|---|---|
| **Analog circuit** | A circuit whose behavior is judged through continuous electrical quantities such as voltage, current, gain, and noise. | Correctness is usually specification- and simulation-based rather than a simple output match. |
| **SPICE** | A family of circuit-description and simulation tools used to analyze electronic circuits. | SPICE feedback can ground circuit generation, repair, sizing, and optimization. |
| **Schematic** | A logical diagram of components and electrical connections. | A valid schematic must preserve electrical intent, not merely look plausible. |
| **PCB** | Printed circuit board: the physical board that connects and supports electronic components. | PCB benchmarks may evaluate understanding, placement, routing, or native tool interaction. |
| **BOM** | Bill of materials: the list of parts required to build a design. | Product-level changes may require component identity, availability, cost, and substitution reasoning. |
| **Firmware** | Software that runs close to the hardware, often on a microcontroller or embedded processor. | A hardware change may also require drivers, pin mappings, and firmware updates. |
| **ERC** | Electrical rule check: automated checks for suspicious or invalid electrical connections in a schematic. | Passing ERC catches rule violations but does not prove that the intended function is correct. |
| **DRC** | Design rule check: automated checks that a chip layout or PCB follows geometric and manufacturing rules. | Passing DRC is necessary in many flows, but it is not equivalent to functional correctness. |

## Evaluation and evidence

| Term | Plain-language meaning | Why it matters in this survey |
|---|---|---|
| **Method** | The model, pipeline, or agent proposed to perform a task. | It is the system being evaluated. |
| **Benchmark** | A defined collection of tasks plus the rules for running and scoring them. | A benchmark is an evaluation contract, not just a folder of examples. |
| **Dataset** | The examples or artifacts used by a method or benchmark. | A dataset alone may not specify tools, budgets, success conditions, or metrics. |
| **Oracle** | The independent mechanism used to decide whether an output is correct. | Examples include answer matching, compilation, simulation, formal proof, DRC, or deployment. |
| **Testbench** | Code or infrastructure that stimulates a hardware design and checks observed behavior. | Testbench passing establishes correctness only for the behaviors that were tested. |
| **Simulation** | Execution of a hardware or circuit model without manufacturing the hardware. | It supplies executable feedback but remains limited by the model and test scenarios. |
| **Formal verification** | Mathematical analysis that proves or disproves stated properties within a formal model. | It can provide a stronger oracle than sampled simulation for the properties actually expressed. |
| **Regression** | A collection of tests run together to detect whether a change breaks expected behavior. | Repository-repair benchmarks often use native project regressions as their central oracle. |
| **PPA** | Power, performance, and area: three common chip implementation objectives. | A functionally correct design may still be unusable if its PPA is poor. |
| **PDK** | Process design kit: foundry-provided rules, models, and files for a manufacturing process. | Physical and analog results may not transfer across PDKs and technology nodes. |
| **pass@k** | The probability that at least one of `k` generated candidates passes the evaluator. | Results are not comparable unless `k`, sampling, and the evaluator are reported consistently. |
| **Reproducibility** | The ability for others to repeat an evaluation with enough of the same data, code, tools, and settings. | Commercial tools, missing versions, and unstable repositories can block reproduction. |
| **Contamination or leakage** | Overlap between evaluation material and data available during model training or development. | Public repositories and historical fixes may already be memorized by a model. |

## Interaction and agents

| Term | Plain-language meaning | Why it matters in this survey |
|---|---|---|
| **Single-shot** | The system produces one submitted response without using evaluator feedback. | A simulator run after submission does not by itself make the system an agent. |
| **Iterative** | The system revises an answer over multiple internal steps or rounds. | Iteration may improve results even without access to a native engineering tool. |
| **Tool-using system** | The system can invoke a compiler, simulator, formal tool, EDA engine, or structured API. | Tool use becomes meaningful when returned evidence can change the next action. |
| **Long-horizon agent** | A system that observes, plans, acts, and revises over many environment interactions. | Success depends on the scaffold, permissions, stopping rule, and budget as well as the model. |
| **Agent scaffold** | The software around a foundation model that manages prompts, memory, tools, planning, and control flow. | Two systems using the same model may perform differently because their scaffolds differ. |
| **Budget** | Limits on tokens, candidate samples, tool calls, simulator runs, wall-clock time, or money. | Agent results are unfair to compare when their permitted budgets differ substantially. |

## Reading rule

When a paper reports a benchmark score, read the result as a complete tuple:

```text
method + task input + visible context + tool access + budget + oracle + metric
```

If one of these elements changes, the number may no longer be directly comparable.
