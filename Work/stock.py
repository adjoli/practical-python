from typedproperty import typedproperty, String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
        # TODO: Implementar logica para evitar self.shares < 0

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"
