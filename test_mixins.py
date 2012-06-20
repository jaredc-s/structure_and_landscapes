from unittest import TestCase as TC
from mixins import *


class Simple(object):
    def __init__(self, x):
        self.x = x


class EqualityClass(Simple, KeyedEqualityMixin):
    def __key__(self):
        return self.x


class TestDefault(TC):
    def test(self):
        x, y = Simple(1), Simple(1)
        self.assertFalse(x == y)
        self.assertTrue(x < y or y < x)
        self.assertFalse(hash(x) == hash(y))


class TestEquality(TC):
    def test(self):
        x, y, z = EqualityClass(1), EqualityClass(1), EqualityClass(2)
        self.assertTrue(x == y)
        self.assertFalse(x != y)
        self.assertFalse(x == z)
        self.assertTrue(x != z)


class ComparisonClass(EqualityClass, KeyedComparisonMixin):
    pass


class TestComparision(TC):
    def test(self):
        x, y, z = ComparisonClass(1), ComparisonClass(1), ComparisonClass(2)
        self.assertFalse(x < y)
        self.assertTrue(x <= y)
        self.assertFalse(x > y)
        self.assertTrue(x >= y)
        self.assertTrue(x < z)
        self.assertTrue(x <= z)
        self.assertFalse(x > z)
        self.assertFalse(x >= z)
        self.assertFalse(z < x)
        self.assertFalse(z <= x)
        self.assertTrue(z > x)
        self.assertTrue(z >= x)


class HashClass(EqualityClass, KeyedHashingMixin):
    pass


class TestHash(TC):
    def test(self):
        x, y, z = HashClass(1), HashClass(1), HashClass(2)
        self.assertTrue(hash(x) == hash(y))
        self.assertFalse(hash(x) != hash(y))


if __name__ == "__main__":
    import unittest
    unittest.main()
