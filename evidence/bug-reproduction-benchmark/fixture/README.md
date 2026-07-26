# Invoice fixture

A support report says:

> Some invoices are 5% lower than expected when discounts are disabled.

Product rule:

- Omitting `discount_percent` applies the default 5% promotion.
- Passing an explicit `Decimal("0")` disables the promotion and must preserve the subtotal.

The repository is intentionally small. Treat the report as unverified until reproduced. Do not modify the fixture during the reproduction task.
