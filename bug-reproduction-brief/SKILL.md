---
name: bug-reproduction-brief
version: 1.0.1
description: Turn a vague bug report into a minimal, evidence-backed reproduction before proposing a fix.
tags: [debugging, reproduction, triage, evidence]
---

# Bug Reproduction Brief

Use this skill when a bug report is incomplete, intermittent, environment-specific, or mixed with an assumed cause.

## 1. Record the observed failure

Capture the exact error, incorrect output, timestamp, affected route/command and the smallest known input. Preserve logs without secrets or personal data. Label second-hand descriptions as unverified.

## 2. Identify the environment

Record only facts you can inspect: repository and commit, runtime version, operating system/container, dependency lockfile, relevant feature flags and whether the target is local, test or production. Never guess credentials or production configuration.

## 3. Write expected versus actual behaviour

Use two explicit statements:

```text
Expected: [observable result]
Actual:   [observable result, including status/error]
```

Do not use the suspected cause as either statement.

## 4. Reduce the reproduction

Start from the reported path, then remove unrelated data, services and steps one at a time. Keep the smallest fixture that still fails. If it stops failing, restore the last removed condition and record it.

## 5. Prove repeatability

Run the minimal reproduction at least twice where safe. Record commands and outputs. If the failure is intermittent, report the observed frequency and duration instead of calling it deterministic.

## Output

```markdown
# Bug Reproduction Brief
- Target and commit:
- Environment:
- Report provenance: first-hand / second-hand; verified / unverified at intake
- Expected:
- Actual:
- Minimal steps:
- Minimal fixture:
- Reproduced: yes / no / intermittent
- Evidence:
- Unknowns:
- Safe next hypothesis to test:
```

## Boundaries

- Do not change production data merely to reproduce a bug.
- Do not publish secrets, customer records or private source.
- During this reproduction-only workflow, do not state a root cause or causal explanation, even when one line appears suspicious. Put only a testable candidate under `Safe next hypothesis to test`.
- Stop after a verified reproduction; diagnosis and repair are separate workflows.

## More evidence-first workflows

Free source and updates: https://github.com/skyestrela/ai-agent-skill-preview

Complete engineering pack: https://ai-agent-skills-pack.vercel.app/?utm_source=free-skill&utm_medium=github&utm_campaign=bug-reproduction-brief
