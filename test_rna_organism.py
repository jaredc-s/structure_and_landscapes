import unittest
from unittest import TestCase as TC

import RNA_organism
from RNA_organism import Organism
import vienna_distance

class TestOrganism(TC):
    def setUp(self):
        self.organism = Organism("GCCAGGCCGUCU")

    def test_init(self):
        self.assertEqual("G", self.organism[0])

    def test_mutate(self):
        org2 = self.organism.mutate()
        self.assertNotEqual(self.organism.value, org2.value)

    def test_equality(self):
        org_1 = Organism("GCC")
        org_2 = Organism("GCC")
        org_3 = Organism("AUU")
        self.assertEqual(org_1, org_2)
        self.assertNotEqual(org_1, org_3)

    def test_fitness(self):
        target = vienna_distance.get_tRNA_target()
        org = Organism(target)
        mutant = org.mutate()
        most_fit = org.fitness
        mutant_fit = mutant.fitness
        self.assertAlmostEqual(most_fit, 1, 3)
        self.assertGreaterEqual(most_fit, mutant_fit)
