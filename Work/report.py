# report.py
#
# Exercise 2.4
import csv


def portfolio_cost(filename):
    """Compute de total cost (shares * price) of a portfolio price"""

    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # lê e ignora a primeira linha (cabeçalho)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
        return total_cost


def read_portfolio(filename):
    """Return a list of tuples"""

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # lê e ignora a primeira linha (cabeçalho)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
        return portfolio


def read_portfolio_dict(filename):
    """Return a list of dictionaries"""

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            linha = (row[0], int(row[1]), float(row[2]))
            portfolio.append(dict(zip(header, linha)))
        return portfolio


def read_prices(filename):
    portfolio = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                portfolio[row[0]] = float(row[1])
            except:
                pass
        return portfolio


def make_report(file_portfolio, file_prices):
    prices = read_prices(file_prices)
    portfolio = read_portfolio_dict(file_portfolio)

    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    print(('-' * 10 + ' ') * 4)

    for p in portfolio:
        change = prices[p['name']] - p['price']
        print(f"{p['name']:>10s} {p['shares']:>10d} {p['price']:>10.2f} {change:>10.2f}")


if __name__ == '__main__':
    make_report('Data/portfolio.csv', 'Data/prices.csv')
