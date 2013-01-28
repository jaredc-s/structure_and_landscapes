from unittest import TestCase as TC
import random

from meta_population import MetaPopulation
from population import Population
from ..integer.integer_organism import Organism
from nose.plugins.attrib import attr


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


class TestMetaPopulation(TC):
    def setUp(self):
        self.orgs = [Organism(1), Organism(2),
                     Organism(3), Organism(4)]

        self.pops = [Population(self.orgs) for _ in range(10)]
        self.metapop = MetaPopulation(self.pops, 0.5, 0.5)

    def test_max_fitness(self):
        self.assertAlmostEqual(self.metapop.max_fitness(), 4.0)

    def test_mean_fitness(self):
        self.assertAlmostEqual(self.metapop.mean_fitness(), 2.5)

    def test_length(self):
        self.assertEqual(10, len(self.metapop))

    def test_replicate(self):
        self.metapop.replicate()
        for pop in self.metapop:
            self.assertEqual(8, len(pop))

    def test_remove_random(self):
        self.metapop.replicate()
        self.metapop.remove_at_random()
        for pop in self.metapop:
            self.assertEqual(4, len(pop))

    def test_advance_generation(self):
        self.metapop.advance_generation()

    def test_migrate_simple(self):
        self.metapop.migrate()

    @attr("probabilistic")
    def test_migrate(self):
        "Labels orgs in pop to check for migrations"
        for index, pop in enumerate(self.pops):
            for org in pop:
                org.original_pop = index
        self.metapop.migrate()
        migrations_took_place = any(org.original_pop != index
                for index, pop in enumerate(self.pops)
                for org in pop)
        self.assertTrue(migrations_took_place)

    def test_get(self):
        self.assertEqual(self.metapop[1], self.pops[1])
