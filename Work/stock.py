class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        # TODO: Implementar decorator 'property'

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
        # TODO: Implementar logica para evitar self.shares < 0

    def __repr__(self):
        return f"{self.name:>6s} {self.shares:>6d} {self.price:>6.2f}"


def main():
    import fileparse
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select='name shares price'.split(), types=[str, int, float])

        portfolio = [Stock(s['name'], s['shares'], s['price']) for s in portdicts]

        print(sum(s.cost() for s in portfolio))

if __name__ == '__main__':
    main()