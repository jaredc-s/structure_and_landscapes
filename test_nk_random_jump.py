import unittest
from unittest import TestCase as TC
import nkmodel_random_jump
from nkmodel_random_jump import NKWithGenes
from bitstring import Bitstring

class TestNKWithGenes(TC):
    def setUp(self):
        self.list_of_strings = [Bitstring("010"), Bitstring("100"),
                           Bitstring("001")]

    def test_determine_fitness(self):
        nk = NKWithGenes(2, 1, 3, 3)



class TestModule(TC):
    def test_dependencies(self):
        depend = nkmodel_random_jump.generate_dependencies(2, 1, 3, 3)

        self.assertEqual(len(depend), 3)
        self.assertEqual(len(depend[0]), 3)
        self.assertEqual(len(depend[-1]), 3)

    def test_sub_bitstring(self):
        depend = nkmodel_random_jump.generate_dependencies(2, 2, 3, 3)
        list_of_strings = [Bitstring("010"), Bitstring("100"),
                           Bitstring("001")]

        full = nkmodel_random_jump.generate_sub_bitstring(list_of_strings,
                                                           depend, 2)
        self.assertEqual(len(full), len(list_of_strings))
        self.assertEqual(len(full[0]), 3)
        self.assertEqual(len(full[0][0]), 5)
