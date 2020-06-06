# report.py

from . import tableformat
from . import fileparse
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    with open(filename) as lines:
        portfolio = Portfolio.from_csv(lines)
    return portfolio


def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit('==> Usage: %s <portfile> <pricefile> <format>' % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
