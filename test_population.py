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
        return MockOrganism(self.fitness)


class TestPopulation(TC):
    def setUp(self):
        self.pop = Population([MockOrganism(1), MockOrganism(2),
                                MockOrganism(3), MockOrganism(4)])

    def test_init_nogivensize(self):
        self.assertEqual(self.pop.maxsize, 4)
        
    def test_init_givensize(self):
        population = Population([1, 2, 3, 4], 5)
        self.assertEqual(population.maxsize, 5)

    def test_removal(self):
        population = Population([1, 2, 3], 2)
        population.remove_at_random()
        self.assertEqual(population.size, 2)

    def test_leastfit_removal(self):
        this_pop = Population([MockOrganism(1), MockOrganism(2), 
                               MockOrganism(100)], 1)

        this_pop.remove_least_fit()
        self.assertItemsEqual([100], [org.eval_fit() for org in this_pop])

    def test_replicate(self):
        self.setUp()
        self.pop.replicate()
        self.assertEqual(8, self.pop.size)

    def test_advance(self):
        big_pop = Population([MockOrganism(1), MockOrganism(2), 
                               MockOrganism(90)], 3)
        
        big_pop.advance_generation()
        self.assertLessEqual(big_pop.size, 3)
        
