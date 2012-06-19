import unittest
from unittest import TestCase as TC

import integer_organism as organism
from integer_organism import Organism


class TestOrganism(TC):
    def setUp(self):
        self.value_0 = 0
        self.value_1 = 1
        self.value_2 = 2
        self.bad_value = "0"

    def test_init(self):
        organism = Organism(self.value_0)
        self.assertEqual(organism.value, self.value_0)

        organism2 = Organism(self.value_1)
        self.assertEqual(organism2.value, self.value_1)

    def test_init_exception(self):
        with self.assertRaises(AssertionError):
            Organism(self.bad_value)

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

    def test_fitness(self):
        g0 = Organism(self.value_0)
        self.assertAlmostEqual(0, g0.fitness)
        g1 = Organism(self.value_1)
        self.assertAlmostEqual(1, g1.fitness)


class TestModule(TC):
    def test_default_organism(self):
        org = organism.default_organism
