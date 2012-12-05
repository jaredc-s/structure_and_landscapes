from unittest import TestCase as TC

from fitness_tree import *

class MockOrganism(object):
    def __init__(self, fitness, identifier):
        self.fitness = fitness
        self.identifier = identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __hash__(self):
        return hash(self.identifier)

    def __ne__(self, other):
        return not self == other

class TestModule(TC):

    def setUp(self):
        self.orgs = [MockOrganism(1, "a"),
                MockOrganism(2, "b"),
                MockOrganism(3, "c")]
        self.tree = build_tree(self.orgs)

    def test_build_tree(self):
        self.assertEqual(self.tree.total_fitness, 6)
        self.assertEqual(self.tree.total_leaves, 3)

    def test_tree_to_list(self):
        list_of_orgs = tree_to_list(self.tree)
        self.assertEqual(set(list_of_orgs), set(self.orgs))

    def test_add_to_tree(self):
        org_added = MockOrganism(4, "d")
        new_tree = add_to_tree(self.tree, org_added)
        new_list = tree_to_list(new_tree)

        self.assertEqual(set(new_list), set(self.orgs + [org_added]))
        self.assertEqual(self.tree.total_fitness, 10)
        self.assertEqual(self.tree.total_leaves, 4)

    def test_remove_leaf_uniformly_all(self):
        removed_orgs = []
        tree = self.tree
        for _ in range(len(self.orgs)):
            tree, org = remove_leaf_uniformly(tree)
            removed_orgs.append(org)
        self.assertEqual([], tree_to_list(self.tree))
        self.assertEqual(set(removed_orgs), set(self.orgs))

    def test_remove_leaf_uniformly_exception(self):
        for _ in range(len(self.orgs)):
            self.tree, _ = remove_leaf_uniformly(self.tree)
        with self.assertRaises(ValueError):
            print(remove_leaf_uniformly(self.tree))

    def test_choose_leaf_by_fitness(self):
        org = choose_leaf_by_fitness(self.tree)
        self.assertIn(org, self.orgs)
