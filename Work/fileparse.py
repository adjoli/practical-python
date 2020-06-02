# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, select=None) -> list:
    """
    Parse a CSV file in a list of records.

    :param filename:
    :return: list:
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read de file headers
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
                row = [row[index] for index in indices]

            record = dict(zip(headers, row))
            records.append(record)

        return records
