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
        self.assertEqual(True, b[0])
        self.assertEqual(False, b[1])
        self.assertEqual(2, len(b))

    def test_iter(self):
        b = Bitstring("01")
        for pos, expected in zip(b, [True, False]):
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
        b2 = Bitstring([1, 0, 0, 0])
        b3 = Bitstring((True, False, False, False))
        b4 = Bitstring("1")
        self.assertEqual(b, b2)
        self.assertEqual(b, b3)
        self.assertNotEqual(b, b4)

    def test_hash(self):
        b = Bitstring("000")
        b_ = Bitstring("101")
        self.assertSetEqual({b, b_},
                            {Bitstring("000"), Bitstring("101")})

    def test_int(self):
        b = Bitstring('110110')
        c = Bitstring('0000')
        d = Bitstring('')
        e = Bitstring('10')
        self.assertEqual(int(b), 54)
        self.assertEqual(int(c), 0)
        self.assertEqual(int(d), 0)
        self.assertEqual(int(e), 2)

    def test_selected_loci_as_int(self):
        b = Bitstring('110110')
        pos_0 = b.selected_loci_as_int([0])
        self.assertEqual(0, pos_0)
        pos_123 = b.selected_loci_as_int([1,2,3])
        self.assertEqual(3, pos_123)
        pos_1 = b.selected_loci_as_int([1])
        self.assertEqual(1, pos_1)

    def test_single_step_mutant(self):
        bs = Bitstring("00")
        mutant = bs.single_step_mutant()
        self.assertNotEqual(bs, mutant)

class TestModule(unittest.TestCase):

    def test_flip_position(self):
        b = Bitstring("00000")
        b_mutated = bitstring.flip_position(b, 0)
        self.assertEqual(b_mutated, Bitstring("00001"))
