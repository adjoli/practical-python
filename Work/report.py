# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv


def read_portfolio(filename: str) -> list:
    """Return a list of tuples"""

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # lê e ignora a primeira linha (cabeçalho)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
        return portfolio


def read_portfolio_dict(filename: str) -> list:
    """
    Return a list of dictionaries
    """
    return parse_csv(filename=filename, has_header=True)


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name,price data
    """
    return parse_csv(filename=filename)


def make_report(file_portfolio: str, file_prices: str) -> None:
    portfolio = parse_csv(file_portfolio, select='name shares price'.split(), types=[str, int, float], has_header=True)
    prices = {chave: valor for chave, valor in read_prices(file_prices)}

    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    print(('-' * 10 + ' ') * 4)

    for p in portfolio:
        change = float(prices[p['name']]) - p['price']
        print(f"{p['name']:>10s} {p['shares']:>10d} {p['price']:>10.2f} {change:>10.2f}")


if __name__ == '__main__':
    make_report('Data/portfoliodate.csv', 'Data/prices.csv')
