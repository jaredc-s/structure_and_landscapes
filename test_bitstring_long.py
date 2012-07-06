import unittest
from unittest import TestCase

import bitstringLong
from bitstringLong import Bitstring

class TestBitstringLong(TestCase):
    def test_init(self):
        b = Bitstring('1001')
        print b
        self.assertEqual(len(b), 4)
        self.assertEqual(b[0], str(1))

    def test_int(self):
        b = Bitstring('100')
        self.assertEqual(int(b), 4)

    def test_string(self):
        b = Bitstring('1000000')
        self.assertEqual(str(b), '1000000')

class TestModule(TestCase):
    def test_mutate_position(self):
        b = Bitstring('1010111')
        b_mutate = bitstringLong.flip_positions(b, (2,3))
        self.assertEqual(b_mutate.value, 91 )
        
