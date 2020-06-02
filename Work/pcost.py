# pcost.py
#
# Exercise 1.27
import csv


def portfolio_cost(filename: str) -> float:
    """Compute de total cost (shares * price) of a portfolio price"""

    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_num, row in enumerate(rows, start=1):
            try:
                record = dict(zip(header, row))
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {row_num}: Bad row: {row}")
        return total_cost
