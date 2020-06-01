# report.py
#
# Exercise 2.4
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
    """Return a list of dictionaries"""

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            registro = dict(zip(header, row))
            registro['shares'] = int(registro['shares'])
            registro['price'] = float(registro['price'])
            portfolio.append(registro)
        return portfolio


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name,price data

    :param filename:
    :return: dict
    """
    portfolio = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                portfolio[row[0]] = float(row[1])
            except:
                pass
        return portfolio


def make_report(file_portfolio: str, file_prices: str) -> None:
    prices = read_prices(file_prices)
    portfolio = read_portfolio_dict(file_portfolio)

    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    print(('-' * 10 + ' ') * 4)

    for p in portfolio:
        change = prices[p['name']] - p['price']
        print(f"{p['name']:>10s} {p['shares']:>10d} {p['price']:>10.2f} {change:>10.2f}")


if __name__ == '__main__':
    make_report('Data/portfoliodate.csv', 'Data/prices.csv')
