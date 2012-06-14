import unittest
from unittest import TestCase as TC

import integer_genome
from integer_genome import Genome


class TestGenome(TC):
    def test_init(self):
        genome = Genome(0)
        self.assertEqual(genome.value, 0)

        genome2 = Genome(-4)
        self.assertEqual(genome2.value, -4)

    def test_init_exception(self):
        with self.assertRaises(AssertionError):
            Genome("1")

    def test_eq(self):
        g0 = Genome(0)
        g0_ = Genome(0)
        g1 = Genome(1)
        self.assertEqual(g0, g0_)
        self.assertNotEqual(g0, g1)

        i = 0
        self.assertFalse(g0 == i)
        self.assertTrue(g0 != i)

    def test_hash(self):
        set_of_genomes = {Genome(0), Genome(1)}
        set_of_genomes2 = {Genome(1), Genome(2)}
        set_of_genomes3 = set_of_genomes.union(set_of_genomes2)

        self.assertSetEqual(set_of_genomes3, {Genome(0), Genome(1), Genome(2)})


class TestModule(TC):
    def test_default_genome(self):
        genome = integer_genome.default_genome
