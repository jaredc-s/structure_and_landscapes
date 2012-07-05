import unittest
from unittest import TestCase as TC

import rna_organism
from rna_organism import Organism
import vienna_distance


class TestOrganism(TC):
    def setUp(self):
        self.organism = rna_organism.default_organism

    def test_mutate(self):
        org2 = self.organism.mutate()
        self.assertNotEqual(self.organism.value, org2.value)

    def test_fitness(self):
        self.assertAlmostEqual(self.organism.fitness, 1)
        all_As = "".join('A' for _ in self.organism.value)

        a_org = Organism(all_As)
        self.assertLess(a_org.fitness, self.organism.fitness)


class TestModule(TC):
    def test_default(self):
        def_org = rna_organism.default_organism
        self.assertEqual(vienna_distance.get_tRNA_sequence(), def_org.value)
