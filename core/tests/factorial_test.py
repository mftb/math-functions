from unittest import TestCase
from core.factorial import factorial


class FactorialTest(TestCase):

    def test_fact_0(self):
        assert factorial(0) == 1

    def test_fact_1(self):
        assert factorial(1) == 1

    def test_fact_2(self):
        assert factorial(2) == 2

    def test_fact_10(self):
        assert factorial(10) == 10 * factorial(9)

    def test_multitest(self):
        for i in range(1, 20):
            assert factorial(i) == i * factorial(i - 1)
