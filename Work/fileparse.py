# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, select=None, types=None) -> list:
    """
    Parse a CSV file in a list of records.

    :param filename:
    :return: list:
    """
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue

            if indices:
                if types:
                    row = [func(row[index]) for func, index in zip(types, indices)]
                else:
                    row = [row[index] for index in indices]

            record = dict(zip(headers, row))
            records.append(record)

        return records


if __name__ == '__main__':
    print(parse_csv('Data/portfolio.csv', select='name price'.split(), types=[str, float]))
