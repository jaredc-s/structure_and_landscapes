import unittest
from unittest import TestCase as TC
import nk_model
import nk_organism
from nk_organism import Organism
import bitstring
import random
import mutate


class TestOrganism(TC):
    def setUp(self):
        self.value = bitstring.Bitstring("100")
        self.lookup = [[1, 0.5], [0.2, 0.4], [0.1, 0.8]]
        deps = [[0], [1], [2]]
        self.model = nk_model.NKModelSimple(deps, self.lookup)
        self.org = Organism(self.value, self.model)

    def test_init(self):
        self.assertEqual(self.org.value, self.value)

    def test_fitness(self):
        expected_fit = (1 + 0.2 + 0.8) / float(3)
        self.assertEqual(expected_fit, self.org.fitness)

    def test_equality(self):
        other = Organism(bitstring.Bitstring("001"), self.model)
        self.assertNotEqual(self.org, other)
        self.assertEqual(self.org, self.org)

    def test_mutate(self):
        other = self.org.mutate()
        self.assertNotEqual(self.org, other)
