# Survey manuscript workspace

This directory maps the research library to the future paper. Manuscript prose should be written only after the supporting cards reach at least `source-checked` status.

## Proposed paper structure

| Section | Purpose | Evidence dependency |
|---|---|---|
| 1. Introduction | Motivate the need for a benchmark-centered survey | Cross-direction synthesis and prior-survey comparison |
| 2. Scope and methodology | Define search, inclusion, coding, and verification procedures | Research protocol and audit log |
| 3. Taxonomy | Explain stages and cross-cutting evaluation axes | Taxonomy definitions and adjudicated examples |
| 4. RTL generation and verification | Compare generation, debugging, and formal tasks | RTL and formal benchmark/method cards |
| 5. HLS, synthesis, and physical design | Cover tool-driven front-to-back flows | HLS and physical-design cards |
| 6. Analog, schematic, and PCB | Cover circuit and board-level tasks | Analog/SPICE and PCB cards |
| 7. Repository and system-scale agents | Analyze context, interaction, and cross-artifact work | Repair, co-design, and agent-system cards |
| 8. Evaluation methodology | Compare oracles, metrics, budgets, leakage, and reproducibility | Cross-benchmark evidence matrix |
| 9. Gaps and research agenda | State evidence-backed open problems | Findings supported across multiple directions |
| 10. Conclusion | Summarize the field without introducing new claims | Frozen manuscript evidence set |

## Planned paper assets

| Asset | Content | Source of truth |
|---|---|---|
| Figure 1 | Field overview across hardware-design stages | Direction map |
| Figure 2 | Evolution from single-shot generation to tool-interactive agents | Year and interaction fields in benchmark cards |
| Figure 3 | Benchmark anatomy: input → system → artifact → oracle | Verified benchmark cards |
| Table 1 | Prior survey comparison | `docs/related-surveys.md` after source audit |
| Table 2 | Main benchmark catalog | Frozen export of `data/benchmarks.csv` plus card fields |
| Table 3 | Oracle and reproducibility comparison | Cross-benchmark evidence matrix |
| Figure 4 | Capability coverage and research gaps | Adjudicated capability coding |

## Writing rule

No paragraph should be supported only by the original deep-research draft. The draft is a discovery aid. Paper claims must resolve to primary-source evidence recorded in the research library.
