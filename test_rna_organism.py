import unittest
from unittest import TestCase as TC

import rna_organism
from rna_organism import Organism

class TestOrganism(TC):
    def setUp(self):
        self.organism = Organism("GCCAGGCCGUCU")

    def test_init(self):
        self.assertEqual("G", self.organism[0])

    def test_mutate(self):
        org2 = self.organism.mutate()
        self.assertNotEqual(self.organism.value, org2.value)
