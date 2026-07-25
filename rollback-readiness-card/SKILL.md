---
name: rollback-readiness-card
version: 1.0.0
description: Create a concise rollback card with immutable release identity, data compatibility and measurable kill criteria before deployment.
tags: [deployment, rollback, release, operations]
---

# Rollback Readiness Card

Use this skill before a release where rollback must be fast and unambiguous.

## 1. Identify both releases

Record the candidate commit/image/deployment identifier and the last known good identifier. A branch name or “latest” tag is not immutable evidence.

## 2. Check data compatibility

List migrations, backfills, queue/message changes, cache formats and external API contracts. State whether old code can safely read data written by the new release. If rollback needs a data repair, provide a separate reviewed procedure rather than hiding it in one command.

## 3. Record the actual rollback command

Use the platform's real command or dashboard action. Verify target, permissions and expected output without performing the production rollback. Never invent identifiers or credentials.

## 4. Define kill criteria

Use measurable signals and windows, for example:

- error rate above a stated threshold for a stated duration;
- checkout or login journey failing in a real probe;
- latency above a stated percentile threshold;
- data integrity check returning a mismatch;
- worker backlog growing beyond a stated limit.

Name who or what is authorised to trigger rollback.

## 5. Verify post-rollback checks

List health, smoke, data and queue checks that prove the old release is serving correctly. A successful rollback command alone is not recovery evidence.

## Output

```markdown
# Rollback Readiness Card
- Environment:
- Candidate release:
- Last known good release:
- Data/schema compatibility:
- Rollback action:
- Authorised trigger:
- Kill criteria and window:
- Post-rollback checks:
- Known irreversible effects:
- READY / BLOCKED:
```

## Boundaries

- Do not execute a production rollback while preparing the card.
- Do not reverse destructive migrations without a verified data recovery plan.
- Do not claim readiness when the last known good release is unknown.
- Keep credentials out of the card.

## More evidence-first workflows

Free source and updates: https://github.com/skyestrela/ai-agent-skill-preview

Complete engineering pack: https://ai-agent-skills-pack.vercel.app/?utm_source=free-skill&utm_medium=github&utm_campaign=rollback-readiness-card
