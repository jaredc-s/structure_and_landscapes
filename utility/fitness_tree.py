"""
Implementation of a Data Structure that allows births to be choosen
in proportion to fitness (fecundity selection) and random death.

Weighted (by fitness) binary tree.

Could be improved by making the tree a class, instead of data and functions.
"""
from __future__ import division
import random


class Node(object):
    """
    Primary Component of the tree.

    Holds 4 attributes.
    The total fitness of its children
    The total number of leaves
    The Node to the Left
    The Node to the Right
    The leaf contents (if the Node is a leaf, the organism)
    """

    def __init__(self, left, right, leaf_contents=None):
        self.left = left
        self.right = right
        self.leaf_contents = leaf_contents
        self.calibrate_totals()

    def calibrate_totals(self):
        if self.leaf_contents is not None:
            self.total_fitness = self.leaf_contents.fitness
            self.total_leaves = 1
        else:
            self.total_fitness = 0.0
            self.total_leaves = 0
            if self.left is not None:
                self.total_fitness += self.left.total_fitness
                self.total_leaves += self.left.total_leaves
            if self.right is not None:
                self.total_fitness += self.right.total_fitness
                self.total_leaves += self.right.total_leaves


def choose_leaf_by_fitness(tree):
    """
    Returns the contents of a leaf (an org) choosen randomly,
    in proportion to fitness.
    """
    if tree_is_empty(tree):
        raise ValueError("Can't choose from empty tree.")
    if tree.leaf_contents is not None:
        return tree.leaf_contents
    if tree.left is not None and tree.right is not None:
        if should_choose_left_by_fitness(tree):
            return choose_leaf_by_fitness(tree.left)
        else:
            return choose_leaf_by_fitness(tree.right)
    if tree.left is not None:
        return choose_leaf_by_fitness(tree.left)
    else:
        return choose_leaf_by_fitness(tree.right)


def should_choose_left_by_fitness(tree):
    """
    Return True randomly in proportion to the fitness
    of the leaves.
    """
    return should_choose_first_weighted(
        tree.left.total_fitness, tree.right.total_fitness)


def should_choose_left_by_number_of_leaves(tree):
    """
    Return True randomly in proportion to the number of leaves (uniformly).
    """
    return should_choose_first_weighted(
        tree.left.total_leaves, tree.right.total_leaves)


def should_choose_first_weighted(weight_a, weight_b):
    """
    Returns True randomly in proportion to the weight of a relative to b.
    """
    return random.random() < (weight_a / (weight_a + weight_b))


def remove_leaf_uniformly(tree):
    """
    Removes a leaf from the tree randomly, and not with respect to fitness.
    Every leaf has an equal chance of being removed.
    Returns the tree and the org removed.
    """
    if tree_is_empty(tree):
        raise ValueError("Can't remove from empty tree.")
    if tree.leaf_contents is not None:
        org, tree.leaf_contents = tree.leaf_contents, None
        return tree, org
    if tree.left is not None and tree.right is not None:
        if should_choose_left_by_number_of_leaves(tree):
            new_left, removed_org = remove_leaf_uniformly(tree.left)
            if tree_is_empty(new_left):
                tree.left = None
            else:
                tree.left = new_left
        else:
            new_right, removed_org = remove_leaf_uniformly(tree.right)
            if tree_is_empty(new_right):
                tree.right = None
            else:
                tree.right = new_right
        tree.calibrate_totals()
        return tree, removed_org

    if tree.left is not None or tree.right is not None:
        if tree.left is not None:
            subtree = tree.left
        else:
            subtree = tree.right
        return remove_leaf_uniformly(subtree)


def tree_is_empty(tree):
    return (tree.left is None and
            tree.right is None and
            tree.leaf_contents is None)


def tree_to_list(tree):
    """
    Returns all of the leaf contents (orgs) as a list.
    """
    list_to_populate = []
    if tree.left is not None:
        list_to_populate += tree_to_list(tree.left)
    if tree.leaf_contents is not None:
        list_to_populate.append(tree.leaf_contents)
    if tree.right is not None:
        list_to_populate += tree_to_list(tree.right)
    return list_to_populate


def build_tree(orgs):
    """
    Returns a tree from an iterable of organisms.
    """
    tree = empty_tree()
    for org in orgs:
        tree = add_to_tree(tree, org)
    return tree


def singleton_tree(org):
    """
    Returns a Node with the organism.
    """
    return Node(left=None, right=None, leaf_contents=org)


def empty_tree():
    """
    Returns a tree lacking any orgs
    """
    return Node(left=None, right=None)


def add_to_tree(tree, org):
    """
    Adds a single org to a tree.
    """
    return merge_trees(tree, singleton_tree(org))


def merge_trees(tree_master, tree_other):
    """
    Adds the tree_other to the tree_master.
    """

    if tree_master.left is None and tree_master.right is None:
        # Tree master is leaf, convert to non-leaf.
        if tree_master.leaf_contents is None:
            return tree_other
        else:
            return Node(left=tree_master, right=tree_other)

    if tree_master.left is None or tree_master.right is None:
        # Tree master is one sided, add other to right
        if tree_master.left is None:
            tree_master.left = tree_master.right
        tree_master.right = tree_other
    else:
        # Tree master is full, add to lighter side
        if tree_master.left.total_fitness < tree_master.right.total_fitness:
            tree_master.left = merge_trees(tree_master.left, tree_other)
        else:
            tree_master.right = merge_trees(tree_master.right, tree_other)
    tree_master.calibrate_totals()
    return tree_master
