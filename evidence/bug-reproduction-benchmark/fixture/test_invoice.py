import unittest
from decimal import Decimal

from invoice import invoice_total


class InvoiceTotalTests(unittest.TestCase):
    def test_default_discount(self) -> None:
        self.assertEqual(invoice_total(Decimal("100.00")), Decimal("95.00"))

    def test_explicit_ten_percent_discount(self) -> None:
        self.assertEqual(
            invoice_total(Decimal("100.00"), Decimal("10")),
            Decimal("90.00"),
        )


if __name__ == "__main__":
    unittest.main()
