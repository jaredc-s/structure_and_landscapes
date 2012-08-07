from unittest import TestCase as TC
import bitstring_organism
from bitstring_organism import Organism
import bitstring
from bitstring import Bitstring
import random


class TestOrganism(TC):
    def setUp(self):
        self.value_0 = Bitstring("000")
        self.value_1 = Bitstring("001")
        self.value_2 = Bitstring("111")
        self.bad_value = "000"

    def test_init(self):
        organism = Organism(self.value_0)
        self.assertEqual(organism.value, self.value_0)

        organism2 = Organism(self.value_1)
        self.assertEqual(organism2.value, self.value_1)

    def test_eq(self):
        g0 = Organism(self.value_0)
        g0_ = Organism(self.value_0)
        g1 = Organism(self.value_1)
        self.assertEqual(g0, g0_)
        self.assertNotEqual(g0, g1)

        self.assertFalse(g0 == self.bad_value)
        self.assertTrue(g0 != self.bad_value)

    def test_hash(self):
        set_of_organisms = {Organism(self.value_0), Organism(self.value_1)}
        set_of_organisms2 = {Organism(self.value_1), Organism(self.value_2)}
        set_of_organisms3 = set_of_organisms.union(set_of_organisms2)

        self.assertSetEqual(
            set_of_organisms3,
            {Organism(self.value_0), Organism(self.value_1),
                Organism(self.value_2)})

    def test_mutate(self):
        g0 = Organism(self.value_0)
        g_ = g0.mutate()
        self.assertNotEqual(g0, g_)

    def test_parent(self):
        g0 = Organism(self.value_0)
        g_ = g0.mutate()
        self.assertEqual(g0.id, g_.parent)

    def test_fitness(self):
        g0 = Organism(self.value_0)
        self.assertAlmostEqual(0, g0.fitness)
        g1 = Organism(self.value_1)
        self.assertAlmostEqual(1, g1.fitness)

    def test_repr(self):
        org = Organism(Bitstring('1001'))
        expected = "Organism(value=Bitstring('1001'))"
        self.assertEqual(repr(org), expected)


class TestModule(TC):
    def test_default_organism(self):
        org = bitstring_organism.default_organism
