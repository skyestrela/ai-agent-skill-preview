# Free AI Agent Skills for Coding Workflows

[![skills.sh](https://img.shields.io/badge/skills.sh-4%20free%20skills-111827)](https://skills.sh/skyestrela/ai-agent-skill-preview/code-review-gate)
[![MIT](https://img.shields.io/badge/licence-MIT-0f766e)](LICENSE)

Four complete, readable Markdown workflows for Claude Code, Codex, Hermes and other coding agents: structured pre-merge review, evidence-backed bug reproduction, dependency-risk triage and rollback readiness.

**Product Hunt launch:** [AI Agent Skills Pack — 10 evidence-first workflows for AI coding agents](https://www.producthunt.com/products/ai-agent-skills-pack?launch=ai-agent-skills-pack). Questions and concrete workflow feedback are welcome; no testimonial or purchase is required.

**Download all four free workflows:** [Free Bundle v1.0.0](https://github.com/skyestrela/ai-agent-skill-preview/releases/tag/free-workflows-bundle-v1.0.0) — one verified MIT-licensed ZIP, or inspect each Markdown file below.

This repository publishes complete free skills from the **AI Agent Skills Pack** on a measured release cadence. They are not teaser files: all current workflows are MIT licensed and usable on their own.

## Install a skill

Verified one-command Codex installation:

```bash
npx skills add skyestrela/ai-agent-skill-preview --skill code-review-gate --agent codex --global --yes --copy
```

Install the Bug Reproduction Brief instead:

```bash
npx skills add skyestrela/ai-agent-skill-preview --skill bug-reproduction-brief --agent codex --global --yes --copy
```

Install Dependency Risk Triage:

```bash
npx skills add skyestrela/ai-agent-skill-preview --skill dependency-risk-triage --agent codex --global --yes --copy
```

Install Rollback Readiness Card:

```bash
npx skills add skyestrela/ai-agent-skill-preview --skill rollback-readiness-card --agent codex --global --yes --copy
```

List the available skill without installing:

```bash
npx skills add skyestrela/ai-agent-skill-preview --list
```

Or generate the skill prompt directly:

```bash
npx skills use skyestrela/ai-agent-skill-preview@code-review-gate
```

Manual installation is also supported: read `code-review-gate/SKILL.md`, place the folder in the location supported by your agent, then ask the agent to use `code-review-gate` before a merge or release. Skill discovery paths vary by product and version, so follow your agent's current documentation.

## What it checks

- hardcoded secrets and unsafe patterns;
- authentication and authorisation gaps;
- injection risks;
- missing error handling;
- correctness and async problems;
- dead or overly complex code;
- review evidence and ship/no-ship verdict.

## Free skills

<!-- FREE_SKILLS_START -->
- [Code Review Gate](code-review-gate/SKILL.md) — evidence-first security, correctness and quality review before merge.
- [Bug Reproduction Brief](bug-reproduction-brief/SKILL.md) — turns a vague bug report into a minimal, evidence-backed reproduction before fixes begin.
- [Dependency Risk Triage](dependency-risk-triage/SKILL.md) — separates vulnerable, reachable dependencies from noisy scanner output and verifies upgrades.
- [Rollback Readiness Card](rollback-readiness-card/SKILL.md) — records release identity, rollback commands, data compatibility and kill criteria before deployment.
<!-- FREE_SKILLS_END -->

## Complete pack

The complete £19 pack contains ten workflows:

1. Code Review Gate
2. Debug Tracer
3. TDD Enforcer
4. PR Shipper
5. Security Sweep
6. API Scaffold
7. Migration Doctor
8. Deploy Checker
9. Refactor Plan
10. Incident Post-Mortem

Product page and secure Stripe Checkout:

https://ai-agent-skills-pack.vercel.app/?utm_source=github&utm_medium=free-preview&utm_campaign=skills-pack-v1

The paid pack is a one-time single-user commercial licence with a 30-day refund policy.

## Verified compatibility

- The public repository is detected by the current `skills` CLI as four installable skills.
- A clean isolated Codex install placed `SKILL.md` under `~/.agents/skills/code-review-gate/`.
- The source remains plain Markdown and can be inspected before installation.
- The workflow requires evidence before approval and does not auto-fix security findings.
- `examples/EXAMPLE-REPORT.md` shows the expected report shape against an explicitly unsafe fixture.

## Safety

These are written workflows, not executable software or a security/compliance certification. Review commands for your environment and keep destructive or production actions behind explicit approval.

## Licence

This free preview is MIT licensed. The complete paid pack uses the licence included with the download.
