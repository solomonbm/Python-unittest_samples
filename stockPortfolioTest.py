from stockPortfolio import *
import stockPortfolio
import io
import unittest

class PortfolioTestBase(unittest.TestCase):
    """Base class for all Portfolio tests."""

    def assertCostEqual(self, p, cost):
        """Assert that 'p''s cost is equal to 'cost'."""
        self.assertEqual(p.cost(), cost)

class PortfolioTest(PortfolioTestBase):
    def test_emprty(self):
        p = Portfolio()
        self.assertCostEqual(p, 0.0)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertCostEqual(p, 17648.0)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100, 36.15)
        self.assertCostEqual(p, 21263.0)

    def test_bad_input(self):
        p = Portfolio()
        with self.assertRaises(TypeError):
            p.buy("IBM")

class PortfolioSellTest(PortfolioTestBase):
    def __init__(self, *args, **kwargs):
        super(PortfolioSellTest, self).__init__(*args, **kwargs)
        self.p = Portfolio()
    
    #Invoked before each test method
    def setUp(self):        
        self.p.buy("MSFT", 100, 27.0)
        self.p.buy("DELL", 100, 17.0)
        self.p.buy("ORCL", 100, 34.0)        

    def test_sell(self):
        self.p.sell("MSFT", 50)
        self.assertCostEqual(self.p, 6450.0)

    def test_not_enough(self):
        with self.assertRaises(ValueError):
            self.p.sell("MSFT", 200)

    def test_dont_own_it(self):
        with self.assertRaises(ValueError):
            self.p.sell("IBM", 1)

class FakeUrlLib(object):
    def StringIO(self, url):
        return io.StringIO("'IBM',140\n'HPQ',32\n")        
    
class PortfolioValueTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PortfolioValueTest, self).__init__(*args, **kwargs)
        self.p = Portfolio()
        
    def setUp(self):
        # Save the urllib.request, and install our fake.
        self.old_urllib = stockPortfolio.io
        stockPortfolio.io = FakeUrlLib()
                        
        self.p.buy("IBM", 100, 120.0)
        self.p.buy("HPQ", 100, 30.0)

    def test_value(self):
        self.assertEqual(self.p.value(), 17200.0)

    def taerDown(self):
        # Restore the real urllib.request
        stockPortfolio.urllib.request = self.old_urllib
        
if __name__ == '__main__':
    unittest.main(exit=False)
