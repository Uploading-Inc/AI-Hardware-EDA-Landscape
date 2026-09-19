# Related surveys

This project builds on several important surveys of large language models for electronic design automation. The purpose of the comparison is not to rank them, but to make the intended contribution of the new survey explicit.

| Survey | Year | Main organizing view | Role in this project |
|---|---:|---|---|
| [LLM4EDA: Emerging Progress in Large Language Models for Electronic Design Automation](https://arxiv.org/abs/2401.12224) | 2024 | Assistant chatbots, HDL/script generation, and verification/analysis | Historical baseline and early map of the field |
| [A Survey of Research in Large Language Models for Electronic Design Automation](https://doi.org/10.1145/3715324) | 2025 | Broad LLM-for-EDA methods, customization, and applications | General terminology and application-level coverage |
| [Large Language Models for EDA: From Assistants to Agents](https://doi.org/10.1561/1000000063-2) | 2025 | Transition from passive assistants to autonomous agents | Foundation for comparing interaction regimes |
| [Large Language Models for EDA: Future or Mirage?](https://doi.org/10.1145/3736167) | 2025 | Code generation, verification/debugging, knowledge, and optimization | Broad task taxonomy and critical assessment |

## Why another survey?

The earlier surveys establish the field, but most predate the rapid growth of 2026 work on repository-scale repair, board-level schematic generation, PCB understanding and routing, hardware–software co-design, and tool-interactive physical-design agents.

This project therefore emphasizes a different unit of analysis: **the benchmark and its evaluation contract**. For each work, we ask what context the system receives, whether it can interact with tools, what artifacts it must produce, how correctness is checked, how realistic the task is, and whether the evaluation can be reproduced.

The intended contribution is not only a longer bibliography. It is a benchmark-centered account of what current results actually demonstrate and which comparisons remain invalid or unsupported.

## Current boundary

This page is an initial positioning note. The final survey will expand the search, verify publication metadata, compare inclusion criteria, and cite the exact taxonomy and conclusions of each prior survey from its primary text.
