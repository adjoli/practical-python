import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOGL', 100, 490.1)
        self.assertEqual(s.name, 'GOOGL')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock('GOOGL', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock('GOOGL', 100, 490.1)
        self.assertEqual(s.shares, 100)
        s.sell(50)
        self.assertEqual(s.shares, 50)
        # s.sell(60)  # Tentativa de vender mais ações do que tem
        # self.assertEqual(s.shares, 0)

    def test_bad_shares(self):
        s = stock.Stock('GOOGL', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'


if __name__ == '__main__':
    unittest.main()