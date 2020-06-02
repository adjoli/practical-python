# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, selected_cols=[]) -> list:
    """
    Parse a CSV file in a list of records.

    :param filename:
    :return: list:
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read de file headers
        headers = next(rows)

        # Check if selected_cols are in headers
        sel_cols = []
        if selected_cols:
            sel_cols = [c for c in selected_cols if c in headers]

        records = []
        for row in rows:
            if not row:
                continue

            record = dict(zip(headers, row))

            if sel_cols:
                my_record = {}
                for col in sel_cols:
                    my_record[col] = record[col]
                record = my_record

            records.append(record)

        return records
