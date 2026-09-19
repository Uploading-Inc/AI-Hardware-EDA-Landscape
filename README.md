<div align="center">

# AI × Hardware / EDA Landscape

**A living, evidence-grounded map of benchmarks and agents for hardware engineering**

[![Status](https://img.shields.io/badge/status-research%20in%20progress-7c3aed?style=flat-square)](#project-status)
[![Catalog](https://img.shields.io/badge/catalog-22%20seed%20systems-2563eb?style=flat-square)](data/benchmarks.csv)
[![Cutoff](https://img.shields.io/badge/literature%20cutoff-2026--09--19-0f766e?style=flat-square)](#scope)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-f59e0b?style=flat-square)](LICENSE)

[Landscape](#landscape-at-a-glance) · [Taxonomy](docs/taxonomy.md) · [Data](data/benchmarks.csv) · [Research notes](docs/research-notes.md) · [Blog](blog/from-rtl-generation-to-engineering-agents.md) · [Contribute](CONTRIBUTING.md)

</div>

This repository studies how AI systems are evaluated when they **design, understand, verify, debug, optimize, or operate electronic hardware workflows**. It covers RTL and formal verification, HLS, physical design, analog/SPICE, schematics, PCB design, and hardware–software co-design.

The central observation is simple: the field no longer lacks hardware benchmarks in general. It lacks benchmarks that test **integrated engineering work** across repositories, tools, executable verification, and heterogeneous artifacts.

> This is a working research repository, not yet the companion site of a released paper. Every entry should eventually be traceable to a primary paper, official project page, and—where available—released code or data.

## Project status

The current release establishes the research structure and imports a 22-system seed catalog from an initial deep-research pass. The next phase is source-by-source verification, followed by a manuscript-quality systematic comparison.

| Track | Current state | Next milestone |
|---|---|---|
| Literature map | Seed catalog assembled | Verify every row against primary sources |
| Taxonomy | Five evaluation axes defined | Test inter-rater consistency on edge cases |
| Blog | First synthesis draft available | Add figures and source-complete citations |
| Paper | Outline and evidence base only | Freeze protocol before full screening |
| Reproducibility | Machine-readable CSV + validator | Add provenance and archived snapshots |

## Landscape at a glance

The most useful distinction is not only *which EDA stage* a benchmark covers, but *what kind of engineering capability it actually measures*.

| Axis | Lower-complexity setting | Higher-complexity setting |
|---|---|---|
| Context scale | Isolated module or question | Full repository or system |
| Interaction | Single-shot generation | Long-horizon tool-using agent |
| Oracle strength | Text/reference similarity | Simulation, formal, physical, or deployment checks |
| Artifact breadth | One HDL or netlist file | RTL, verification, configuration, software, and board artifacts |
| Engineering realism | Synthetic textbook task | Historical issue, native project, or real EDA environment |

Across the initial catalog, the literature appears to move through four regimes:

1. **Generation-centric evaluation** — specification-to-RTL benchmarks such as VerilogEval and RTLLM.
2. **Verification-grounded evaluation** — formal, simulation, synthesis, or SPICE checks replace surface similarity.
3. **Repository- and system-scale evaluation** — models must reason over real projects and coordinate changes.
4. **Environment-grounded agents** — systems plan, act, inspect tool feedback, and repair their work.

The remaining gap is an end-to-end benchmark combining existing project understanding, engineering-change requests, component and datasheet selection, schematic/PCB edits, firmware changes, native EDA use, and executable validation.

## Coverage map

| Area | Representative systems | What is measured |
|---|---|---|
| RTL generation | VerilogEval, RTLLM, CVDP | Specification-to-HDL correctness and quality |
| Formal verification | FVEval, AssertLLM, AssertLLM2 | Assertion generation, provability, coverage, bug detection |
| Repository repair | RTL-Repo, RTL-BenchLS, HWE-Bench-Repair | Long-context completion or issue-to-patch workflows |
| HLS and co-design | HLS-Eval, HSCO-Bench | Synthesizable C/C++, accelerator integration, deployment |
| Physical design | ChatEDA, PDAGENT-BENCH, FluxBench | Tool use, scripts, reports, P&R, ECO, cost-efficiency |
| Analog/SPICE | AnalogGym, AnalogCoder, NetlistBench, SpiceDiff-Agent | Sizing, structural edits, simulation-guided repair |
| Board and PCB | HWE-Bench-Schematic, PCB-QA, PCBWorld | Component-aware schematics, understanding, native routing |

The complete seed catalog is maintained in [`data/benchmarks.csv`](data/benchmarks.csv). Field definitions and evidence rules are in [`data/SCHEMA.md`](data/SCHEMA.md).

## Scope

Included work must make electronic or hardware design, verification, debugging, optimization, or tool operation central to the evaluated task. Generic software-engineering benchmarks and “hardware for AI” papers are out of scope unless the AI system itself performs a hardware-engineering task.

The literature cutoff for the current snapshot is **2026-09-19**. Because recent work is preprint-heavy, venue, code, and dataset availability should be rechecked before any archival release.

## Repository layout

```text
.
├── README.md                         # Project landing page and current synthesis
├── blog/                             # Public-facing essays derived from the evidence
├── data/
│   ├── benchmarks.csv                # Machine-readable benchmark catalog
│   └── SCHEMA.md                     # Field definitions and evidence requirements
├── docs/
│   ├── research-notes.md             # Research protocol, caveats, and open questions
│   └── taxonomy.md                   # Classification framework
├── scripts/
│   └── validate_catalog.py           # Lightweight catalog integrity checks
├── CITATION.cff
├── CONTRIBUTING.md
└── LICENSE
```

## Working principles

- Prefer primary papers, official repositories, and venue records.
- Separate what a benchmark **claims** from what its released evaluator **executes**.
- Record model, scaffold, tools, budgets, and environment—not only the model name.
- Treat “open source not located” as uncertainty, not evidence of non-release.
- Distinguish tasks mined from GitHub from tasks that actually expose repository context.
- Avoid “first,” “best,” and “state of the art” unless the comparison boundary is explicit.

## Validation

Run the catalog checks with the Python standard library:

```bash
python3 scripts/validate_catalog.py
```

The validator checks required fields, controlled vocabularies, duplicate IDs, years, and URL shape. It does not replace source verification.

## Citation

This project does not yet have an archival paper. Until then, cite the repository metadata in [`CITATION.cff`](CITATION.cff) and include the accessed revision. A paper-specific BibTeX entry will be added after public preprint release.

## Acknowledgments

The repository structure draws on patterns used by research releases from Google Research, Microsoft Research, NVIDIA Research, and Meta Research: a concise project-facing README, explicit methodology, machine-readable artifacts, reproducible evaluation instructions, and clear citation and contribution paths.

## License

Text and structured research data are released under the [Creative Commons Attribution 4.0 International License](LICENSE), unless a file states otherwise. Linked papers, codebases, datasets, figures, and trademarks remain under their respective owners' terms.
