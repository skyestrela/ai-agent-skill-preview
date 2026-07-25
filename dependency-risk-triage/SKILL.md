---
name: dependency-risk-triage
version: 1.0.0
description: Triage dependency alerts by version, reachability and verified upgrade impact instead of blindly updating everything.
tags: [dependencies, security, supply-chain, testing]
---

# Dependency Risk Triage

Use this skill when a scanner, advisory or platform reports vulnerable or outdated dependencies.

## 1. Establish the real dependency state

Inspect the manifest and lockfile. Record package manager, locked version, direct or transitive status and the command that proves it. Do not rely on an old dashboard screenshot.

## 2. Verify the advisory

Record advisory identifier, affected version range, fixed version and source. Distinguish an official advisory from an unverified post. Check whether the vulnerable package and code path are present in the shipped artifact.

## 3. Rank practical exposure

For each finding, record:

- reachable in production, development-only or unknown;
- attacker-controlled input required;
- authentication or network boundary;
- confidentiality, integrity and availability impact;
- existing mitigation;
- confidence and missing evidence.

A high scanner score with an unreachable code path is not the same as a proven exploit. An unknown path is not safe; it needs investigation.

## 4. Choose the smallest safe upgrade

Prefer the minimum supported version that fixes the advisory. Read release and migration notes. Avoid blanket major-version upgrades unless the smaller path is unavailable.

## 5. Verify in a reversible branch

Update the lockfile in an isolated branch. Run dependency audit, targeted tests, full relevant tests and a build. Compare runtime/bundle behaviour where relevant. Do not deploy automatically.

## Output

```markdown
# Dependency Risk Triage
- Advisory and source:
- Locked / fixed version:
- Direct or transitive:
- Reachability:
- Practical impact:
- Proposed minimum upgrade:
- Tests/build run:
- Result:
- Residual risk or blocker:
```

## Boundaries

- Never expose private registry tokens or audit output containing credentials.
- Do not mark an advisory fixed because installation succeeded.
- Do not delete lockfiles to force a convenient resolution.
- Production rollout requires the project's normal approval and rollback process.

## More evidence-first workflows

Free source and updates: https://github.com/skyestrela/ai-agent-skill-preview

Complete engineering pack: https://ai-agent-skills-pack.vercel.app/?utm_source=free-skill&utm_medium=github&utm_campaign=dependency-risk-triage
