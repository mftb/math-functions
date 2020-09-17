from unittest import TestCase
from core.fibonacci import fibonacci_naive, fibonacci


class FibonacciTest(TestCase):

    def test_fibonacci(self):
        for i in range(0, 1000):
            assert fibonacci_naive(i) == fibonacci(i)
