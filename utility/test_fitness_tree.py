from unittest import TestCase as TC

from fitness_tree import *

class MockOrganism(object):
    def __init__(self, fitness, identifier):
        self.fitness = fitness
        self.identifier = identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __ne__(self, other):
        return not self == other

class TestModule(TC):

    def test_build_tree(self):
        orgs = [MockOrganism(1, "a"),
                MockOrganism(2, "b"),
                MockOrganism(3, "c")]
        tree = build_tree(orgs)
        self.assertEqual(tree.total_fitness, 6)
        self.assertEqual(tree.total_leaves, 3)
