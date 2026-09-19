# Research notes and protocol

## Provenance

The seed synthesis was prepared from the user-provided working document `deep-research-report (1).md`, dated 2026-09-19. That document is treated as a discovery artifact, not as publication-ready evidence: it contains internal citation placeholders from a research tool and therefore must not be quoted as a source.

The public repository preserves its substantive map—candidate papers, taxonomy, initial comparisons, and open questions—while requiring every claim to be revalidated against a primary source.

## Research question

How has evaluation of AI for hardware design evolved from isolated generation toward repository-scale, tool-interactive, verifier-grounded engineering, and which capabilities remain unmeasured?

## Inclusion criteria

A work is included when all applicable conditions hold:

1. It was publicly available by the stated literature cutoff.
2. Electronic or hardware design, verification, debugging, optimization, or tool operation is central.
3. It defines an evaluable task, dataset, environment, or protocol—or systematically surveys such work.
4. Inputs, outputs, and scoring are described well enough to compare with other systems.

Benchmark-bearing systems may be included when their evaluation suite reveals a distinct benchmark design, even if the paper's main contribution is a method.

## Exclusion criteria

- Generic software or CAD benchmarks without electronic-design relevance.
- AI accelerator papers whose research question is only how to run AI efficiently.
- Training corpora without a meaningful evaluation protocol.
- Security-only challenge sets that do not evaluate general hardware-engineering capability.
- Vendor demonstrations without an inspectable scholarly or technical evaluation.

## Source hierarchy

Use sources in this order:

1. Archival paper or latest author-approved preprint.
2. Official code, dataset, or project repository.
3. Official venue or institutional publication record.
4. Secondary scholarly survey for discovery and terminology.

Blog posts, social media, and repository summaries can help discovery but should not anchor quantitative claims.

## Per-paper extraction card

Each verified entry should record:

- canonical title and disambiguated short name;
- year, venue, paper URL, code URL, and data URL;
- hardware stage and task definition;
- input and output artifacts;
- dataset size and provenance;
- verifier/oracle and success metric;
- interaction regime and tool access;
- repository context and engineering realism;
- headline result with its precise experimental setting;
- limitations stated by the authors and limitations inferred by this review;
- verification date and reviewer initials.

## Current synthesis

The initial evidence suggests four transitions:

1. **From output resemblance to execution.** Compile, simulation, formal, synthesis, DRC, and deployment increasingly replace text similarity.
2. **From modules to projects.** Repository-scale tasks expose fault localization, dependency reasoning, and multi-file coordination failures hidden by isolated exercises.
3. **From models to systems.** Tool interfaces, scaffolds, budgets, and environment design can materially change results even with the same foundation model.
4. **From one artifact to engineering change.** The frontier is no longer only generating HDL; it is coordinating intent across artifacts and verification loops.

## Open questions

- How should benchmark leakage be measured when source projects and fixes are public?
- Which oracle combinations best approximate engineering acceptance without making evaluation prohibitively expensive?
- How should tool-call, token, simulator, and wall-clock budgets be normalized?
- Can repository-scale hardware tasks remain reproducible when commercial EDA tools are required?
- What is the smallest realistic benchmark for a coupled board-plus-firmware change?
- How should human review be incorporated when electrical validity is necessary but not sufficient for design intent?

## Near-term work plan

1. Verify the 22 seed rows against primary sources.
2. Add claim-level provenance and evidence excerpts without copying copyrighted text.
3. Freeze taxonomy and screening protocol before expanding the search.
4. Run forward/backward citation expansion from the strongest benchmark papers.
5. Produce figures only after the underlying table is stable.
6. Convert the synthesis into a paper outline and a series of focused blog posts.
