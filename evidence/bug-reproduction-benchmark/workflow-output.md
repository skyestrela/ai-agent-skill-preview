**Bug Reproduction Brief**

- Target and commit: local fixture, commit `a4b9eab9dcc7b2ebbfe5f5d0502d4866cefd36ce`
- Intake provenance: support report in `README.md` was second-hand and unverified at intake; the issue is now first-hand verified
- Environment: Linux WSL2, `python3 3.14.3`, local-only repository, no dependency lockfile present in the tree, no feature flags observed

- Observed failure:
  - Timestamp: `2026-07-26T13:37:14Z`
  - Command: `python3 - <<'PY' ... invoice_total(Decimal('100.00'), Decimal('0')) ... PY`
  - Output: `95.00`
  - Affected path: `invoice.py`

- Expected vs actual:
  - Expected: explicit `Decimal("0")` disables the promotion and preserves the subtotal
  - Actual: `invoice_total(Decimal("100.00"), Decimal("0"))` returned `95.00`

- Minimal steps:
  1. Run `python3 - <<'PY'` with:
     ```python
     from decimal import Decimal
     from invoice import invoice_total
     print(invoice_total(Decimal("100.00"), Decimal("0")))
     ```
  2. Observe `95.00`

- Minimal fixture:
  - `invoice_total(Decimal("100.00"), Decimal("0"))`

- Reproduced status:
  - Reproduced twice with identical output: `95.00`
  - Existing tests passed: `python3 -m unittest -v test_invoice.py`

- Evidence:
  - Report text: `README.md`
  - Implementation entry point: `invoice.py`

- Unknowns:
  - Whether the same behavior appears for other explicit zero-valued inputs such as `Decimal("0.00")` was not tested
  - No external services, production data, or secrets were involved

- Safe next hypothesis to test:
  - Check whether the function distinguishes `None` from an explicit zero-valued `discount_percent` argument in this code path
