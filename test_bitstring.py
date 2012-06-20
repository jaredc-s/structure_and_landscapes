"""
This module tests the bitstring class.
"""
import unittest
import copy

import bitstring
from bitstring import Bitstring


class TestBitstring(unittest.TestCase):

    def test_init(self):
        b = Bitstring("01")
        self.assertEqual(True, b[1])
        self.assertEqual(False, b[0])
        self.assertEqual(2, len(b))

    def test_iter(self):
        b = Bitstring("01")
        for pos, expected in zip(b, [False, True]):
            self.assertEqual(pos, expected)

    def test_eq(self):
        b = Bitstring("10")
        b2 = Bitstring("10")
        b3 = Bitstring("100")
        b4 = Bitstring("11")
        self.assertTrue(b == b2)
        self.assertTrue(b != b3)
        self.assertTrue(b != b4)

        s = "10"
        self.assertFalse(b == s)

    def test_hamming_distance(self):
        b = Bitstring("10101")
        b2 = Bitstring("10101")
        b3 = Bitstring("01010")
        self.assertEqual(b.hamming_distance(b2), 0)
        self.assertEqual(b.hamming_distance(b3), 5)

    def test_repr(self):
        b = Bitstring("10")
        b_as_str = repr(b)
        b2 = eval(b_as_str)
        self.assertEqual(b, b2)

    def test_copy(self):
        b = Bitstring("10101")
        b_copy = copy.copy(b)
        self.assertEqual(b, b_copy)

    def test_init_from_iterable(self):
        b = Bitstring("0001")
        b2 = Bitstring([0, 0, 0, 1])
        b3 = Bitstring((False, False, False, True))
        self.assertEqual(b, b2)
        self.assertEqual(b, b3)

    def test_hash(self):
        b = Bitstring("000")
        b_ = Bitstring("101")
        self.assertSetEqual({b, b_},
                            {Bitstring("000"), Bitstring("101")})


class TestModule(unittest.TestCase):

    def test_mutate_positions(self):
        b = Bitstring("00000")
        b_mutated = bitstring.flip_positions(b, (0, 3, 4))
        self.assertEqual(b_mutated, Bitstring("10011"))
