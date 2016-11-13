import io
import csv
import requests

class Portfolio(object):
    """A simple stock portfolio"""
    def __init__(self):
        # stocks is a list of lists:
        # [[name, shares, price], ...]
        self.stocks = []

    def buy(self, name, shares, price):
        """Buy 'name': 'shares' sharesa at 'price'. """
        self.stocks.append([name, shares, price])

    def cost(self):
        """What was the total cost of this portfolio?"""
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares * price
        return amt

    def sell(self, name, shares):
        """Sell 'shares' amount of 'name' shares."""        
        for holding in self.stocks:
            if holding[0] == name:
                if holding[1] < shares:
                    raise ValueError("Not enough shares")
                holding[1] -= shares
                break
        else:
            raise ValueError("You don't own that stock")

    def current_prices(self):
        """Return a dict mapping names to current prices."""
        url = "http://finance.yahoo.com/d/quotes.csv?f=sl1&s="
        url += ",".join(sorted(s[0] for s in self.stocks))        
        data = io.StringIO(requests.get(url).text)
        dialect = csv.Sniffer().sniff(data.read(1024))
        data.seek(0)
        reader = csv.reader(data, dialect)        
        return { name: float(currPrice) for name, currPrice in reader}

    def value(self):
        """Return the current value of the portfolio."""
        prices = self.current_prices()
        total = 0.0
        for name, shares, _ in self.stocks:
            total += shares * prices[name]
        return total
            
