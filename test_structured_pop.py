import unittest
from unittest import TestCase as TC

import structure_population
from structure_population import Structured_Population
import random

class MockOrganism(object):
    def __init__(self, value):
        self.fitness = value

    def eval_fit(self):
        return self.fitness

    def mutate(self):
        return MockOrganism(self.fitness)

class MockPopulation(object):
    def __init__(self, orgs, maxsize=None):
        self.pop = list(orgs)
        self.max_size = maxsize
    def __len__(self):
        return len(self.pop)
    
    def replicate(self):
        xmen = [org.mutate() for org in self.pop]
        self.pop += xmen

    def remove_at_random(self):
        if len(self.pop) > self.max_size:
            self.pop = [random.choice(self.pop) for i in range(self.max_size)]

class TestPopulation(TC):
    def setUp(self):
        self.orgs = [MockOrganism(1), MockOrganism(2),
                     MockOrganism(3), MockOrganism(4)]
        
        self.pops = [MockPopulation(self.orgs, 4) for i in range(10)]
        self.struct = Structured_Population(self.pops)

    def test_replicate(self):
        self.struct.replicate()
        for pop in self.struct:
            self.assertEqual(8,len(pop))

    def test_remove_random(self):
        self.struct.replicate()
        self.struct.remove_at_random()
        for pop in self.struct:
            self.assertEqual(4,len(pop))

    def test_migrate(self):
        pass
        
