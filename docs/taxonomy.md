# Taxonomy

This taxonomy is designed to compare benchmark *capabilities*, not merely group papers by EDA stage. A single benchmark may receive multiple domain labels, but every coded field must be justified by the task definition and evaluator.

## Five primary axes

### 1. Context scale

| Level | Operational definition |
|---|---|
| Isolated | One prompt, module, circuit, or question with no surrounding project context |
| Multi-file | Several related artifacts are visible, but the complete native project is not required |
| Repository | The task exposes a real or reconstructed repository and its dependencies |
| System | Success requires coordination across hardware, software, tools, or deployment targets |

### 2. Interaction regime

| Level | Operational definition |
|---|---|
| Single-shot | One model response produces the submitted artifact |
| Iterative | The system revises outputs, but does not operate a native environment |
| Tool-using | The model invokes compilers, simulators, formal tools, EDA tools, or structured APIs |
| Long-horizon agent | The system plans and acts over multiple steps with environment feedback |

An evaluator running a simulator after generation does **not** make the evaluated model a tool-using agent.

### 3. Oracle strength

From weakest to strongest:

1. Textual similarity or answer matching.
2. Syntax, parsing, or compilation.
3. Simulation or testbench execution.
4. Formal, equivalence, or mutation-based verification.
5. Physical checks, full-flow implementation, or real deployment.

Different oracle types are not always strictly comparable. For example, a formal property may be stronger for a local invariant while FPGA deployment may cover a broader system path.

### 4. Artifact breadth

Code whether a task substantively edits or generates each artifact class:

- RTL/HDL
- Assertions and verification collateral
- HLS or software code
- Netlists and SPICE
- EDA scripts and configuration
- Schematics, layout, PCB, and BOM data
- Firmware and drivers
- Build, integration, or deployment artifacts

### 5. Engineering realism

| Level | Evidence |
|---|---|
| Synthetic | Handwritten or generated task without native project history |
| Curated | Expert-authored task reflecting realistic requirements |
| Mined | Derived from open-source artifacts or historical changes |
| Native | Executed in the original project/tool environment |
| Deployed | Evaluated on a physical or production-like target |

## Domain labels

`rtl`, `formal`, `hls`, `logic-synthesis`, `physical-design`, `analog`, `spice`, `schematic`, `pcb`, `hardware-software-codesign`, and `multi-domain`.

## Coding rules

- Code only capabilities explicitly exercised by the benchmark.
- Use `partial` when a capability is present only indirectly; explain why in notes.
- “Real repo” means the evaluated system receives repository-scale context, not merely that examples were mined from GitHub.
- “Verification” requires an external check tied to task success. Self-critique alone does not qualify.
- Preserve name collisions explicitly. The two unrelated works called HWE-Bench are labeled `HWE-Bench-Repair` and `HWE-Bench-Schematic` in this repository.

## Proposed capability matrix

Future coding will use the following binary/partial dimensions:

| Capability | Question |
|---|---|
| Repository understanding | Must the system locate and reason across a project? |
| Requirement interpretation | Is natural-language engineering intent central? |
| Component selection | Must real components or datasheets be selected? |
| Schematic/PCB editing | Must an existing board artifact be modified? |
| Firmware integration | Must embedded software change with hardware? |
| Native EDA use | Does the system interact with a real engineering tool? |
| Executable verification | Is success machine-checked beyond text similarity? |
| Iterative debugging | Can tool feedback alter subsequent actions? |
| Cross-artifact change | Must multiple artifact types change coherently? |

