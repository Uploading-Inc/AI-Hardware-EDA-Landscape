# Benchmark catalog schema

`benchmarks.csv` is the canonical machine-readable index. It is intentionally compact in the seed release; evidence-level fields will be added after source verification.

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable, lowercase identifier used by this repository |
| `name` | string | Display name; disambiguated where names collide |
| `year` | integer | First public paper/preprint year |
| `domain` | enum | Primary hardware/EDA domain |
| `task` | string | Short description of the evaluated task |
| `interaction` | enum | `single-shot`, `iterative`, `tool-using`, or `long-horizon-agent` |
| `oracle` | enum | Strongest central evaluator used for task success |
| `repo_context` | boolean | Whether the evaluated system receives repository-scale context |
| `paper_url` | URL | Canonical paper or venue page |
| `code_url` | URL/blank | Official implementation or benchmark repository, if located |
| `status` | enum | `seed`, `verified`, or `needs-review` |
| `notes` | string | Concise caveat or distinguishing fact |

## Evidence policy

`seed` means the entry came from the initial research pass and still requires a source audit. `verified` should be used only after the paper and release artifacts have been checked. `needs-review` marks a conflict, ambiguity, or unavailable primary source.

Headline numbers do not belong in the canonical table until their task split, model/scaffold, budget, and metric have been verified.

