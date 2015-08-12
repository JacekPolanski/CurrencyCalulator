__author__ = 'jacek'


class CurrencyCalculator:
    def __init__(self):
        self.euro_exchange_rate = 0
        self.pound_exchange_rate = 0
        self.dollar_exchange_rate = 0

    def set_euro_exchange_rate(self, value):
        self.euro_exchange_rate = value

    def set_pound_exchange_rate(self, value):
        self.pound_exchange_rate = value

    def set_dollar_exchange_rate(self, value):
        self.dollar_exchange_rate = value

    def convert_euro_to_pln(self, amount):
        return self.euro_exchange_rate*amount

    def convert_pound_to_pln(self, amount):
        return self.pound_exchange_rate*amount

    def convert_dollar_to_pln(self, amount):
        return self.dollar_exchange_rate*amount