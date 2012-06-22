import unittest
from unittest import TestCase as TC

import nk_organism
from nk_organism import Organism

class TestOrganism(TC):
    def test_init(self):
        Organism('1110', MockLookUpTable.create_table())

class MockLookUpTable(object):
    def __init__(self, n=3, k=1):
        self.n = n
        self.k = k

    def create_table(self):
        return [[i for i in range(2 ** (k + 1))] for _ in range(n)]
