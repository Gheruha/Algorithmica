"""
Q1. You get a list of transactions as dictionaries:
tx = [
  {"id": 1, "amount": "100.50", "currency": "EUR"},
  {"id": 2, "amount": "40", "currency": "EUR"},
  {"id": 3, "amount": None, "currency": "EUR"},
]
Write a Python function that:
- converts amount to float (invalid or missing amounts → treat as 0.0),
- returns the total sum of amounts.
"""

tx = [
    {"id": 1, "amount": "100.50", "currency": "EUR"},
    {"id": 2, "amount": "40", "currency": "EUR"},
    {"id": 3, "amount": None, "currency": "EUR"},
]


def total_amount(tx):

    def to_float(x):
        try:
            return float(x)
        except (TypeError, ValueError):
            return 0.0

    return sum(to_float(t.get("amount")) for t in tx)


print(total_amount(tx))
