from unittest import TestCase
from core.ackermann import ackermann, ackermann_naive


class AckermannTest(TestCase):

    def test_ackermann(self):
        for i in range(0, 4):
            for j in range(0, 10):
                assert ackermann_naive(i, j) == ackermann(i, j)

    def test_ackermann_4_0(self):
        assert ackermann(4, 0) == 13

    def test_ackermann_4_1(self):
        assert ackermann(4, 1) == 65533
