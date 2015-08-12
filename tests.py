# -*- coding: utf-8 -*-
__author__ = 'jacek'

import unittest
from currency_calculator import CurrencyCalculator


class TestCurrencyCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = CurrencyCalculator()

    def test_currency_calculator_has_euro_exchange_rate(self):
        assert self.calculator.euro_exchange_rate != None, \
            "currency_calculator euro_exchange_rate is None"

    def test_currency_calculator_has_pound_exchange_rate(self):
        assert self.calculator.pound_exchange_rate != None, \
            "currency_calculator pound_exchange_rate is None"

    def test_currency_calculator_has_dollar_exchange_rate(self):
        assert self.calculator.dollar_exchange_rate != None, \
            "currency_calculator dollar_exchange_rate is None"

    def test_currency_calculator_set_euro_exchange_rate(self):
        self.calculator.set_euro_exchange_rate(4.1)
        assert self.calculator.euro_exchange_rate == 4.1, \
            "currency_calculator euro_exchange_rate did not set"

    def test_currency_calculator_set_pound_exchange_rate(self):
        self.calculator.set_pound_exchange_rate(4.6)
        assert self.calculator.pound_exchange_rate == 4.6, \
            "currency_calculator pound_exchange_rate did not set"

    def test_currency_calculator_set_dollar_exchange_rate(self):
        self.calculator.set_dollar_exchange_rate(3.7)
        assert self.calculator.dollar_exchange_rate == 3.7, \
            "currency_calculator dollar_exchange_rate did not set"

    def test_currency_calculator_convert_euro_to_pln(self):
        self.calculator.set_euro_exchange_rate(4.1)
        assert self.calculator.convert_euro_to_pln(1) == 4.1, \
            "currency_calculator convert euro to pln failed"
        assert self.calculator.convert_euro_to_pln(3) == 3*4.1, \
            "currency_calculator convert euro to pln failed"

    def test_currency_calculator_convert_pound_to_pln(self):
        self.calculator.set_pound_exchange_rate(4.6)
        assert self.calculator.convert_pound_to_pln(1) == 4.6, \
            "currency_calculator convert pound to pln failed"
        assert self.calculator.convert_pound_to_pln(3) == 3*4.6, \
            "currency_calculator convert pound to pln failed"

    def test_currency_calculator_convert_dollar_to_pln(self):
        self.calculator.set_dollar_exchange_rate(4.6)
        assert self.calculator.convert_dollar_to_pln(1) == 4.6, \
            "currency_calculator convert dollar to pln failed"
        assert self.calculator.convert_dollar_to_pln(3) == 3*4.6, \
            "currency_calculator convert dollar to pln failed"

if __name__=="__main__":
    unittest.main()