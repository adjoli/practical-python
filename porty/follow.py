import os
import time

#print(os.getcwd())

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('../Work/Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
