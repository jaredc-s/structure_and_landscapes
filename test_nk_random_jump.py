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
        contrib_table = [[0.25, 0.8, 0.15], [0.9, 0.4, 0.55], [0.05, 0.7, 0.3]]
        nk = NKWithGenes(1, 1, 2, 2)
        bit_org = Bitstring("0101")
        self.assertNotEqual(0, nk.determine_fitness(bit_org))

    def test_gene_divider(self):
        gene = Bitstring("101010101010")
        nk = NKWithGenes(2, 2, 3, 4)
        divided = nk.divide_to_genes(gene)

        self.assertEqual(len(divided), 4)
        self.assertEqual(len(divided[0]), 3)
        self.assertEqual(Bitstring("010"), divided[-1])

class TestModule(TC):
    def setUp(self):
        self.depend = nkmodel_random_jump.generate_dependencies(2, 2, 3, 3)
        self.list_of_strings = [Bitstring("010"), Bitstring("100"),
                           Bitstring("001")]

    def test_dependencies(self):
        self.assertEqual(len(self.depend), 3)
        self.assertEqual(len(self.depend[0]), 3)
        self.assertEqual(len(self.depend[-1]), 3)

    def test_sub_bitstring(self):
        
        full = nkmodel_random_jump.generate_sub_bitstring(self.list_of_strings,
                                                           self.depend, 2)
        self.assertEqual(len(full), len(self.list_of_strings))
        self.assertEqual(len(full[0]), 3)
        self.assertEqual(len(full[0][0]), 5)

    def test_linear_jump(self):
        linear_model = nkmodel_random_jump.generate_linear_bistring(
            self.list_of_strings, 2, 1)
        print linear_model
        self.assertEqual(4, len(linear_model[0][0]))
        self.assertEqual(3, len(linear_model))
        self.assertEqual(3, len(linear_model[0]))
