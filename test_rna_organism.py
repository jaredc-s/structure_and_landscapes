import unittest
from unittest import TestCase as TC

import RNA_organism
from RNA_organism import Organism
import RNA_Sequence
from RNA_Sequence import RNAsequence

class TestOrganism(TC):
    def setUp(self):
        self.organism = Organism("GCCAGGCCGUCU")

    def test_init(self):
        self.assertEqual("G", self.organism[0])

    def test_mutate(self):
        org2 = self.organism.mutate(1)
        self.assertNotEqual(self.organism, org2)
