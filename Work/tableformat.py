class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, data):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """Emit a table in plan-text format"""

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, data):
        for d in data:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format."""

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML format."""

    def headings(self, headers):
        print(f"<tr>{''.join([f'<th>{h}</th>' for h in headers])}</tr>")

    def row(self, data):
        print(f"<tr>{''.join([f'<td>{d}</td>' for d in data])}</tr>")


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)