import unittest
from unittest import TestCase as TC

import RNA_organism
from RNA_organism import Organism

class TestOrganism(TC):
    def setUp(self):
        self.organism = Organism("GCCAGGCCGUCU")

    def test_init(self):
        self.assertEqual("G", self.organism[0])

    def test_mutate(self):
        org2 = self.organism.mutate()
        self.assertNotEqual(self.organism, org2)
