# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, select=None, types=None, has_header=False, delimiter=None) -> list:
    """
    Parse a CSV file in a list of records.

    :param filename:
    :param select: A list of fields to filter
    :param types: A list of types to typecasting
    :param has_header: A flag to inform if data has headers
    :param delimiter:
    :return:
    """

    # Raise an exception if 'select' has been passed, but data has no headers (has_header is False)
    if select and not has_header:
        raise RuntimeError("'select' argument requires column headers")


    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter) if delimiter else csv.reader(f)

        records = []

        if has_header:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        for row in rows:
            if not row:
                continue

            if has_header:
                if indices:
                    if types:
                        row = [func(row[index]) for func, index in zip(types, indices)]
                    else:
                        row = [row[index] for index in indices]
                record = dict(zip(headers, row))
            else:
                record = row

            records.append(record)

        return records


#if __name__ == '__main__':
    #print(parse_csv(filename='Data/portfolio.csv', has_header=True))
    #print(parse_csv(filename='Data/portfolio.csv', select='name shares'.split(), types=[str, int], has_header=True))
    #print(parse_csv(filename='Data/prices.csv'))
    #print(parse_csv(filename='Data/portfolio.dat', delimiter=' ', select='name'.split()))
