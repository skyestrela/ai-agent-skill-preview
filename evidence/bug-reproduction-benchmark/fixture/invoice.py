"""Small invoice calculation fixture for a reproducible agent evaluation."""
from decimal import Decimal


DEFAULT_DISCOUNT_PERCENT = Decimal("5")


def invoice_total(subtotal: Decimal, discount_percent: Decimal | None = None) -> Decimal:
    """Return a currency total after either the default or an explicit discount."""
    applied_discount = discount_percent or DEFAULT_DISCOUNT_PERCENT
    multiplier = (Decimal("100") - applied_discount) / Decimal("100")
    return (subtotal * multiplier).quantize(Decimal("0.01"))
