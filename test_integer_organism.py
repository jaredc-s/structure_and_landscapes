import unittest
from unittest import TestCase as TC

import integer_organism
from integer_organism import Organism


class TestOrganism(TC):
    def test_init(self):
        organism = Organism(0)
        self.assertEqual(organism.value, 0)

        organism2 = Organism(-4)
        self.assertEqual(organism2.value, -4)

    def test_init_exception(self):
        with self.assertRaises(AssertionError):
            Organism("1")

    def test_eq(self):
        g0 = Organism(0)
        g0_ = Organism(0)
        g1 = Organism(1)
        self.assertEqual(g0, g0_)
        self.assertNotEqual(g0, g1)

        i = 0
        self.assertFalse(g0 == i)
        self.assertTrue(g0 != i)

    def test_hash(self):
        set_of_organisms = {Organism(0), Organism(1)}
        set_of_organisms2 = {Organism(1), Organism(2)}
        set_of_organisms3 = set_of_organisms.union(set_of_organisms2)

        self.assertSetEqual(set_of_organisms3, {Organism(0), Organism(1), Organism(2)})

    def test_duplicate(self):
        g0 = Organism(0)
        g1 = Organism(1)
        self.assertEqual(g0, g0.duplicate())
        self.assertNotEqual(g1, g0.duplicate())

    def test_mutate(self):
        g0 = Organism(0)
        g_ = g0.mutate()
        self.assertNotEqual(g0, g_)


class TestModule(TC):
    def test_default_organism(self):
        organism = integer_organism.default_organism
