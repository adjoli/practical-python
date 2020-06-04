class Stock:
    #__slots__ = ('name', 'shares', 'price')  # Restrict attributes
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
        # TODO: Implementar logica para evitar self.shares < 0

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"


def main():
    import fileparse
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select='name shares price'.split(), types=[str, int, float])

        portfolio = [Stock(s['name'], s['shares'], s['price']) for s in portdicts]

        print(portfolio)

        print(sum(s.cost for s in portfolio))

if __name__ == '__main__':
    main()