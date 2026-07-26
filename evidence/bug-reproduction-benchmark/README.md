# Bug Reproduction Brief — transparent paired run

Run date: 2026-07-26

This is a small, synthetic comparison of the same authenticated Codex model (`gpt-5.4-mini`) on the same committed Python fixture.

It is product-development evidence, not a claim that one workflow will improve every agent or repository.

## Question

Does supplying the Bug Reproduction Brief workflow make a vague-bug investigation more complete and auditable than a concise task instruction alone?

## Controls

Both runs used:

- identical fixture commit: `a4b9eab9dcc7b2ebbfe5f5d0502d4866cefd36ce`;
- the same model: `gpt-5.4-mini`;
- read-only Codex sandbox;
- ephemeral sessions with user configuration and repository rules ignored;
- `PYTHONDONTWRITEBYTECODE=1`;
- clean working trees before and after;
- the same instruction not to modify files or propose/implement a fix.

The workflow run additionally received Bug Reproduction Brief v1.0.1.

## Result

A transparent deterministic rubric scored the final outputs:

- concise control: **6 / 14**;
- workflow-assisted run: **14 / 14**.

Both runs:

- identified the failing explicit-zero input;
- stated expected and observed output;
- ran the existing tests;
- provided a runnable reproduction;
- left the fixture unchanged;
- avoided proposing a fix.

The workflow-assisted run additionally recorded:

- the immutable commit;
- inspected runtime environment;
- second-hand/unverified intake provenance;
- an explicit minimal fixture;
- two separate reproductions;
- unknowns;
- a safe next hypothesis;
- a strict reproduction/diagnosis boundary.

The control jumped to a root-cause statement. The final workflow run deliberately stopped at reproducible observations and a testable next hypothesis.

## Cost and verbosity trade-off

Recorded Codex usage:

| Run | Input tokens | Cached input | Output tokens | Reasoning output |
|---|---:|---:|---:|---:|
| Control | 68,604 | 62,720 | 1,400 | 255 |
| Workflow | 74,547 | 67,328 | 4,471 | 2,661 |

The workflow used 8.7% more input tokens and produced a substantially longer answer. The extra completeness is not free; teams should shorten the output template where speed and token use matter more than auditability.

## Product iteration disclosed

The first workflow run scored 12/14. It exposed two weaknesses:

1. the output did not explicitly preserve the report's second-hand/unverified intake provenance;
2. it stated a causal explanation despite the reproduction-only boundary.

The public skill was tightened to v1.0.1, then rerun against the unchanged fixture. The 14/14 result is from that corrected workflow. This is an iterative product-development run, not a blinded academic study.

## Files

- [`fixture/README.md`](fixture/README.md) — support report and product rule
- [`fixture/invoice.py`](fixture/invoice.py) — intentionally faulty implementation
- [`fixture/test_invoice.py`](fixture/test_invoice.py) — existing passing tests
- [`control-prompt.txt`](control-prompt.txt) — control instruction
- [`workflow-prompt.txt`](workflow-prompt.txt) — workflow instruction used in the final run
- [`control-output.md`](control-output.md) — final control answer, with ephemeral `/tmp` paths normalised
- [`workflow-output.md`](workflow-output.md) — final v1.0.1-assisted answer, with ephemeral `/tmp` paths normalised
- [`score.json`](score.json) — criterion-level result and token usage

## Limitations

- One synthetic Python fixture and one paired run.
- Outputs can vary across models and repeated runs.
- The rubric rewards reproduction-brief completeness, not implementation speed or bug-fix quality.
- Token counts include the Codex execution context, not only the visible prompt files.
- No customer, revenue, security or universal productivity claim is made.

Inspect the workflow itself: [`../../bug-reproduction-brief/SKILL.md`](../../bug-reproduction-brief/SKILL.md).

Complete engineering pack: https://ai-agent-skills-pack.vercel.app/?utm_source=github&utm_medium=benchmark&utm_campaign=bug-reproduction-v1-0-1
