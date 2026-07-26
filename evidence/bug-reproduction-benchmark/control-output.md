**Bug Reproduction Brief**

- Reported issue: invoices are still discounted by 5% when discounts are explicitly disabled.
- Root cause is in `invoice.py` line 10:
  - `applied_discount = discount_percent or DEFAULT_DISCOUNT_PERCENT`
  - `Decimal("0")` is falsy, so the code substitutes the default 5% instead of preserving the subtotal.
- The product rule in `README.md` lines 9-10 explicitly says:
  - omitting `discount_percent` applies the 5% promotion
  - passing `Decimal("0")` disables the promotion and must preserve the subtotal

**Minimal repro**
```python
from decimal import Decimal
from invoice import invoice_total

invoice_total(Decimal("100.00"), Decimal("0"))
# observed: Decimal("95.00")
# expected per report: Decimal("100.00")
```

**Evidence**
- `python3 -m unittest -v` passes, but the existing tests only cover the default discount and a nonzero explicit discount.
- Direct call with `Decimal("0")` returned `95.00`, confirming the support report.
