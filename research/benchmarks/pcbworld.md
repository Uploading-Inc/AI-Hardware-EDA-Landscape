# PCBWorld

| Field | Value |
|---|---|
| Research direction | PCB routing and engine-grounded board design |
| Paper | [PCBWorld: A Benchmark Environment for Engine-Grounded PCB Design Automation](https://arxiv.org/abs/2607.05915) |
| Official artifacts | [LGAI-Research/PCBWorld](https://github.com/LGAI-Research/PCBWorld) |
| First public year / venue | 2026 / arXiv |
| Verification status | `source-checked` for environment, dataset families, and evaluation framing; result audit pending |
| Last checked | 2026-09-19 |

## One-sentence definition

PCBWorld is a KiCad-native environment and benchmark for agents that interactively route printed circuit boards under design-rule feedback.

## Why it exists

Text-only or grid-based routing tasks omit the native operations and design-rule engine used by real PCB tools. PCBWorld exposes a grounded action environment and evaluates completed native board files.

## Benchmark anatomy

| Component | Description |
|---|---|
| Evaluation unit | One placed board with nets and routing constraints |
| Input | Native `.kicad_pcb` state, net connectivity, placement, and design rules |
| Expected output | A routed native board produced through interactive actions |
| Dataset source | Two controllable synthetic families plus real open-source boards |
| Scale | 679 real boards, in addition to synthetic benchmark families |
| Interaction | Reinforcement-learning policy or tool-using LLM agent |
| Environment | KiCad-grounded engine exposing native routing operations and DRC feedback |
| Success oracle | Eight engine-checked metrics applied to the completed board |
| Metrics | Connectivity, routing quality, and design-rule-related measures defined by the environment |

## Evaluation pipeline

```mermaid
flowchart LR
    A[Placed KiCad board plus nets and rules] --> B[Routing agent]
    B --> C[Native routing action]
    C --> D[KiCad engine]
    D --> E[Updated board plus DRC feedback]
    E -->|continue| B
    E -->|finish| F[Routed kicad_pcb]
    F --> G[Eight engine-checked metrics]
```

## What it demonstrates

- Whether an agent can operate inside a native PCB routing engine and react to rule feedback.
- A common evaluation substrate for RL, open-loop, tool-using, and conventional routing methods.

## What it does not demonstrate

- Schematic design, component selection, BOM management, firmware changes, or full product-level board modification.
- Electrical functionality beyond the properties represented by routing and engine checks.

## Reproducibility

| Artifact | Availability | Notes |
|---|---|---|
| Paper | Yes | Public preprint |
| Dataset | Yes | Synthetic and real-board assets are represented in the official release |
| Evaluator | Yes | Environment and evaluation code are public |
| Environment | Open | Built on KiCad; exact versions and external components must be pinned |

## Open questions

- How well do routing metrics predict manufacturability and electrical performance?
- Can the environment support tasks that modify an existing schematic and board together?
