# -*- coding: utf-8 -*-
__author__ = 'jacek'

import unittest
from currency_calculator import CurrencyCalculator


class TestCurrencyCalculator(unittest.TestCase):

    __exchange_rate = 4.2

    def setUp(self):
        self.calculator = CurrencyCalculator()

    def test_calculator_has_exchange_rates(self):
        assert self.calculator.euro_exchange_rate is not None, "euro_exchange_rate is None"
        assert self.calculator.pound_exchange_rate is not None, "pound_exchange_rate is None"
        assert self.calculator.dollar_exchange_rate is not None, "dollar_exchange_rate is None"

    def test_calculator_set_exchange_rates(self):
        self.calculator.set_euro_exchange_rate(self.__exchange_rate)
        self.calculator.set_pound_exchange_rate(self.__exchange_rate)
        self.calculator.set_dollar_exchange_rate(self.__exchange_rate)

        assert self.calculator.euro_exchange_rate == self.__exchange_rate, "euro_exchange_rate did not set"
        assert self.calculator.pound_exchange_rate == self.__exchange_rate, "pound_exchange_rate did not set"
        assert self.calculator.dollar_exchange_rate == self.__exchange_rate, "dollar_exchange_rate did not set"

    def test_calculator_converts_to_pln(self):
        self.calculator.set_euro_exchange_rate(self.__exchange_rate)
        self.calculator.set_pound_exchange_rate(self.__exchange_rate)
        self.calculator.set_dollar_exchange_rate(self.__exchange_rate)

        assert self.calculator.convert_euro_to_pln(1) == self.__exchange_rate, "conversion euro to pln failed"
        assert self.calculator.convert_pound_to_pln(1) == self.__exchange_rate, "conversion pound to pln failed"
        assert self.calculator.convert_dollar_to_pln(1) == self.__exchange_rate, "conversion dollar to pln failed"

        assert self.calculator.convert_euro_to_pln(3) == 3*self.__exchange_rate, "conversion euro to pln failed"
        assert self.calculator.convert_pound_to_pln(3) == 3*self.__exchange_rate, "conversion pound to pln failed"
        assert self.calculator.convert_dollar_to_pln(3) == 3*self.__exchange_rate, "conversion dollar to pln failed"

        assert self.calculator.convert_euro_to_pln(3.4) == 3.4*self.__exchange_rate, "conversion euro to pln failed"
        assert self.calculator.convert_pound_to_pln(3.4) == 3.4*self.__exchange_rate, "conversion pound to pln failed"
        assert self.calculator.convert_dollar_to_pln(3.4) == 3.4*self.__exchange_rate, "conversion dollar to pln failed"


if __name__=="__main__":
    unittest.main()