from unittest import TestCase as TC
import random

from structure_population import Structured_Population
from population import Population
from ..integer.integer_organism import Organism


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
        self.maxsize = maxsize

    def __len__(self):
        return len(self.pop)

    def __iter__(self):
        return iter(self.pop)

    def __getitem__(self, key):
        return self.pop[key]

    def __setitem__(self, key, value):
        self.pop[key] = value

    def replicate(self):
        xmen = [org.mutate() for org in self.pop]
        self.pop += xmen

    def remove_at_random(self):
        if len(self.pop) > self.maxsize:
            self.pop = [random.choice(self.pop) for i in range(self.maxsize)]

    def is_full(self):
        return len(self.pop) >= self.maxsize

    def add_to_pop(self, org):
        self.pop.append(org)

    def moran_selection(self):
        self.pop = self.pop

    def mean_fitness(self):
        pass



class TestPopulation(TC):
    def setUp(self):
        self.orgs = [Organism(1), Organism(2),
                     Organism(3), Organism(4)]

        self.pops = [Population(self.orgs) for _ in range(10)]
        self.struct = Structured_Population(self.pops, 0.5, 0.5)

    def test_max_fitness(self):
        self.assertAlmostEqual(self.struct.max_fitness(), 4.0)

    def test_mean_fitness(self):
        self.assertAlmostEqual(self.struct.mean_fitness(), 2.5)

    def test_length(self):
        self.assertEqual(10, len(self.struct))

    def test_replicate(self):
        self.struct.replicate()
        for pop in self.struct:
            self.assertEqual(8, len(pop))

    def test_remove_random(self):
        self.struct.replicate()
        self.struct.remove_at_random()
        for pop in self.struct:
            self.assertEqual(4, len(pop))

    def test_advance_generation(self):
        self.struct.advance_generation()

    def test_migrate(self):
        self.struct.migrate()

    def test_get(self):
        self.assertEqual(self.struct[1], self.pops[1])
