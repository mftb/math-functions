from unittest import TestCase
from core.ackermann import ackermann, ackermann_naive


class AckermannTest(TestCase):

    def test_ackermann(self):
        for i in range(0, 4):
            for j in range(0, 10):
                assert ackermann_naive(i, j) == ackermann(i, j)
