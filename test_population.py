import unittest
from unittest import TestCase as TC

import population
from population import Population

class MockOrganism(object):
    def __init__(self, value):
        self.fitness = value
    
    def eval_fit(self):
        return self.fitness
    
    def mutate(self):
        return self.fitness += 1
    
class TestPopulation(TC):
    def setUo(self):
        self.population =  Population([MockOrganism(1),MockOrganism(2),MockOrganism(3),MockOrganism(4)])

    def test_init_nogivensize(self):
        self.assertEqual(self.population.maxsize, 4)

    def test_init_givensize(self):
        population = Population([1,2,3,4],5)
        self.assertEqual(self.population.maxsize, 5)

    def test_removal(self):
        population = Population([1,2,3],2)
        population.remove_at_random()
        self.assertEqual(population.size,2)

    def test_leastfit_removal(self):
        population = Population([1,20,30,40],2)
        population.remove_least_fit()
        self.assertItemsEqual([40,30],population)
