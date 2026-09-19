# Research directions

The survey is organized by hardware-design stage, while comparisons use the cross-cutting axes in [`docs/taxonomy.md`](../../docs/taxonomy.md).

| Direction | Central question | Representative benchmarks | Worked card | Section status |
|---|---|---|---|---|
| RTL generation | Can a model translate specifications or partial designs into functionally correct HDL? | VerilogEval, RTLLM, CVDP | [VerilogEval](../benchmarks/verilog-eval.md) | Seed |
| Formal verification | Can a model create useful, valid, and behaviorally meaningful verification collateral? | FVEval, AssertLLM, AssertLLM2 | [FVEval](../benchmarks/fveval.md) | Seed |
| Repository-scale RTL | Can a system reason over real project context and produce a valid multi-file repair? | RTL-Repo, RTL-BenchLS, HWE-Bench-Repair | [HWE-Bench-Repair](../benchmarks/hwe-bench-repair.md) | Seed |
| HLS and co-design | Can AI generate synthesizable accelerators and coordinate hardware with software? | HLS-Eval, HSCO-Bench | [HLS-Eval](../benchmarks/hls-eval.md) | Seed |
| Physical design agents | Can an agent interpret EDA state and operate synthesis, placement, routing, or ECO flows? | ChatEDA, PDAGENT-BENCH, FluxBench | [FluxBench](../benchmarks/fluxbench.md) | Seed |
| Analog and SPICE | Can AI preserve circuit structure and satisfy electrical specifications under simulation? | AnalogGym, AnalogCoder, NetlistBench, SpiceDiff-Agent | [NetlistBench](../benchmarks/netlistbench.md) | Seed |
| Schematic and PCB | Can AI understand or generate board artifacts and act inside a PCB design environment? | HWE-Bench-Schematic, PCB-QA, PCBWorld | [PCBWorld](../benchmarks/pcbworld.md) | Seed |

## Required output for each direction

Before a direction is ready to become a manuscript section, it must contain:

1. A plain-language definition and boundary.
2. An original diagram of the typical task/evaluation pipeline.
3. A benchmark comparison table with input, output, scale, interaction, oracle, and availability.
4. A method-family comparison explaining how representative systems work.
5. Evidence-backed findings and explicit limitations.
6. A list of paper assets: section thesis, final table, final figure, and open-problem callout.
