# Contributing

Contributions that improve source accuracy, coverage, or reproducibility are welcome.

## Before opening a pull request

1. Read the inclusion boundary in [`docs/research-notes.md`](docs/research-notes.md).
2. Prefer a primary paper and official repository over a secondary summary.
3. Add or update the machine-readable row in [`data/benchmarks.csv`](data/benchmarks.csv).
4. Explain the task, interaction regime, oracle, and repository-context classification.
5. Run `python3 scripts/validate_catalog.py`.

## Evidence expected

For a new benchmark, include:

- canonical paper or venue URL;
- official code/data URL when available;
- the exact task input and output;
- the strongest central success oracle;
- whether the evaluated system itself uses tools;
- whether full repository context is exposed;
- one concise limitation or ambiguity.

Please avoid unsupported priority or superiority claims. If a paper and repository disagree, record the conflict and mark the row `needs-review`.

## Small, reviewable changes

Keep each pull request focused on one outcome: a new verified entry, a correction, a taxonomy clarification, or a blog/manuscript improvement. Do not combine unrelated catalog expansion and large editorial rewrites.

