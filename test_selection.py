import unittest
from unittest import TestCase as TC

import selection
from selection import *


class MockOrganism(object):
    def __init__(self, fitness, identifier):
        self.fitness = fitness
        self.identifier = identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __ne__(self, other):
        return not self == other

    def fitness(self):
        return self.fitness

    def mutate(self):
        return MockOrganism(self.fitness, self.identifier + "'")


class TestSelection(TC):
    def setUp(self):
        self.pop = [MockOrganism(1, 'A'), MockOrganism(3, 'B'),
                    MockOrganism(2, 'C')]

    def test_previously_present(self):
        new_pop = select(self.pop, 2)

        for org in new_pop:
            self.assertIn(org, self.pop)

    def test_number_of_draws(self):
        number_draws = 2
        new_pop = select(self.pop, number_draws)

        self.assertLessEqual(len(new_pop), number_draws)

    def test_no_duplicates(self):
        new_pop = select(self.pop, 2)
        new_pop_set = set(new_pop)
        self.assertEquals(len(new_pop_set), len(new_pop))


class TestNormalize(TC):
    def test_multiple(self):
        nums = [1, 2, 3]
        norm_nums = selection.normalize(nums)
        self.assertAlmostEqual(1 / float(6), norm_nums[0])
        self.assertAlmostEqual(2 / float(6), norm_nums[1])
        self.assertAlmostEqual(3 / float(6), norm_nums[2])

    def test_empty(self):
        self.assertEqual([], selection.normalize([]))

    def test_one(self):
        nums = [9]
        self.assertEqual([1.0], selection.normalize(nums))


class TestNumberline(TC):
    def setUp(self):
        self.pop = [MockOrganism(1, 'A'), MockOrganism(3, 'B'),
                    MockOrganism(2, 'C')]

    def test_numbers(self):
        numline = selection.numberline(self.pop)
        self.assertEquals([MockOrganism(1, 'A'), 1 / float(6)], numline[0])
        self.assertEquals([MockOrganism(3, 'B'), 4 / float(6)], numline[1])
        self.assertEquals([MockOrganism(2, 'C'), 6 / float(6)], numline[2])


class TestMoran(TC):
    def setUp(self):
        self.pop = [MockOrganism(1, 'A'), MockOrganism(3, 'B'),
                    MockOrganism(2, 'C')]

    def test_moran_len(self):
        moran_death_birth(self.pop, .5)
        self.assertEqual(3, len(self.pop))

    def test_fecundity(self):
        new_org = fecundity_birth_selection(self.pop)
        self.assertIsInstance(new_org, MockOrganism)

    def test_mutation_rate(self):
        moran_death_birth(self.pop, -1)
        self.assertNotEqual(self.pop[0].identifier[-1], "'")
