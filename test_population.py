import unittest
from unittest import TestCase as TC

import population
from population import Population

class TestPopulation(TC):
    def test_init_nogivensize(self):
        population = Population([1,2,3,4])
        self.assertequal(population.maxsize, 4)

    def test_init_givensize(self):
        population = Population([1,2,3,4],5)
        self.assertequal(population.maxsize, 5)

    def test_removal(self):
        population = Population([1,2,3],2)
        population.remove_at_random()
        self.assertequal(population.size,2)
