from follow import follow
import csv
import report
import tableformat


def select_colums(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_colums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, 'name price change'.split())
    return rows


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfile, logfile, fmt):
    portf = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portf)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings('Name Price Change'.split())
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
