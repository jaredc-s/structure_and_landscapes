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


class TestModule(TC):
    def test_default_genome(self):
        genome = integer_genome.default_genome
