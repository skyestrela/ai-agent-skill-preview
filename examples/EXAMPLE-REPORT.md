# Illustrative Code Review Gate output

This is a worked example, not a claim about a live repository or an executed security test.

Given an intentionally unsafe route containing a hardcoded token, a SQL query built by string concatenation and no authorisation check, the skill should produce a report shaped like this:

```markdown
## Code Review: examples/unsafe-user-route.js

**Verdict:** REQUEST CHANGES

### Critical (must fix before merge)
- [ ] Remove the hardcoded service token and rotate it if it was real — `examples/unsafe-user-route.js:2`
- [ ] Replace concatenated SQL with a parameterised query — `examples/unsafe-user-route.js:6`
- [ ] Add an authorisation check before returning user records — `examples/unsafe-user-route.js:4`

### Warning (should fix soon)
- [ ] Handle database errors explicitly rather than relying on framework defaults — `examples/unsafe-user-route.js:6`

### Suggestion (nice to have)
- [ ] Add an integration test covering an unauthorised request.

### Stats
- Files reviewed: 1
- Critical issues: 3
- Warnings: 1
- Suggestions: 1
```

The workflow must inspect actual source and report real file/line evidence when used on a repository. It must not reuse these illustrative findings when they are absent.
