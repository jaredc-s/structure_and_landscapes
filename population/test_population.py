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
        self.orgs = [MockOrganism(1), MockOrganism(2),
                     MockOrganism(3), MockOrganism(4)]

        self.pop = Population(self.orgs)

    def test_init_nogivensize(self):
        self.assertEqual(self.pop.maxsize, 4)

    def test_init_givensize(self):
        population = Population([1, 2, 3, 4], max_size=5)
        self.assertEqual(population.maxsize, 5)

    def test_removal(self):
        population = Population([1, 2, 3], max_size=2)
        population.remove_at_random()
        self.assertEqual(len(population), 2)

    def test_leastfit_removal(self):
        this_pop = Population([MockOrganism(1), MockOrganism(2),
                               MockOrganism(100)], max_size=1)

        this_pop.remove_least_fit()
        self.assertIn(this_pop[0].eval_fit(),
                              [1, 2, 100])
        self.assertEqual(len(this_pop), 1)

    def test_replicate(self):
        self.pop.replicate()
        self.assertEqual(8, len(self.pop))

    def test_advance(self):
        big_pop = Population(
            [MockOrganism(1), MockOrganism(2),
                MockOrganism(90)], 3)

        big_pop.advance_generation()
        self.assertLessEqual(len(big_pop), 3)

    def test_iter_len(self):
        self.assertEqual(4, len(self.pop))

        for org, poporg in zip(self.orgs, self.pop):
            self.assertEqual(org, poporg)

    def test_add_to_pop(self):
        org = MockOrganism(6)
        self.pop.add_to_pop(org)
        self.assertEqual(5, len(self.pop))

    def test_set(self):
        self.pop[2] = MockOrganism(6)
        print self.pop[2]
        self.assertEqual(self.pop[2].eval_fit(), MockOrganism(6).eval_fit())

    def test_full(self):
        self.assertTrue(self.pop.is_full())

    def test_max_fit(self):
        self.assertEqual(self.pop.max_fitness(), MockOrganism(4).eval_fit())

    def test_mean_fit(self):
        self.assertEqual(self.pop.mean_fitness(), 2.5)
