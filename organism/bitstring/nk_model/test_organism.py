from unittest import TestCase as TC
import nk_model
import organism as nk_organism
from organism import Organism
from .. import bitstring
import random


class TestOrganism(TC):
    def setUp(self):
        self.value = bitstring.Bitstring("100")
        self.lookup = [{0:1, 1:0.5}, {0:0.2, 1:0.4}, {0:0.1, 1:0.8}]
        deps = [[0], [1], [2]]
        self.model = nk_model.NKModelSimple(deps, self.lookup)
        self.org = Organism(self.value, nk_model=self.model)

    def test_init(self):
        self.assertEqual(self.org.value, self.value)

    def test_fitness(self):
        expected_fit = (1 + 0.2 + 0.8) / float(3)
        self.assertEqual(expected_fit, self.org.fitness)
