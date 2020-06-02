# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str) -> list:
    """
    Parse a CSV file in a list of records.

    :param filename:
    :return: list:
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read de file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)
        return records
