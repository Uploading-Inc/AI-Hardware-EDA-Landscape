# Contributing

Contributions that improve source accuracy, coverage, or reproducibility are welcome.

## Choose one contribution type

Keep a pull request focused on one of these outcomes:

| Contribution | Use when | Required artifact |
|---|---|---|
| Discovery seed | A relevant work is missing from the landscape | One provisional row in [`data/benchmarks.csv`](data/benchmarks.csv) with `seed` or `needs-review` status |
| Evidence correction | A catalog or card claim conflicts with a primary source | The corrected field plus a link to the paper, official artifact, or venue record |
| Verification upgrade | A seed has been checked deeply enough to support survey writing | A completed [benchmark](research/templates/benchmark-card.md) or [method](research/templates/method-card.md) card and synchronized catalog row |
| Narrative or figure | Verified evidence is ready to become public synthesis | A bounded change to the field guide, evidence matrix, blog, or manuscript plan with links back to supporting cards |

Read the readiness criteria in [`ROADMAP.md`](ROADMAP.md) before promoting an item from discovery into manuscript evidence.

## Before opening a pull request

1. Read the inclusion boundary in [`docs/research-notes.md`](docs/research-notes.md).
2. Prefer a primary paper and official repository over a secondary summary.
3. Add or update the machine-readable row in [`data/benchmarks.csv`](data/benchmarks.csv) when catalog facts change.
4. Explain the task, interaction regime, oracle, and repository-context classification.
5. Use the templates in [`research/templates/`](research/templates/) for new evidence cards or direction briefs.
6. Run both repository checks:

   ```bash
   python3 scripts/validate_catalog.py
   python3 scripts/validate_repository.py
   ```

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

Use repository-relative Markdown links, quoted `src`/`href` attributes in embedded HTML, and properly closed fenced code blocks. The documentation check validates these conventions, benchmark-card structure, local assets, and SVG syntax.

## Small, reviewable changes

Keep each pull request focused on one outcome. Do not combine unrelated catalog expansion, evidence adjudication, and large editorial rewrites. If a correction changes a public synthesis claim, update the evidence card first and the narrative in the same pull request only when the relationship is direct and reviewable.
