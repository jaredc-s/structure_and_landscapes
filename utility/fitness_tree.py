"""
Implementation of a Data Structure that allows births to be choosen
in proportion to fitness (fecundity selection) and random death.

Weighted (by fitness) binary tree.
"""

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
        if self.left is None and self.right is None:
            assert self.leaf_contents is not None
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

def build_tree(orgs):
    """
    Returns a tree from a list of organisms.
    """
    tree = singleton_tree(orgs[0])
    for org in orgs[1:]:
        tree = add_to_tree(tree, singleton_tree(org))
    return tree

def singleton_tree(org):
    """
    Returns a Node with the organism.
    """
    return Node(left=None, right=None, leaf_contents=org)

def add_to_tree(tree_master, tree_other):
    """
    Adds the tree_other to the tree_master.
    """

    if tree_master.left is None and tree_master.right is None:
        # Tree master is leaf, convert to non-leaf.
        return Node(left = tree_master, right = tree_other)

    if tree_master.left is None or tree_master.right is None:
        # Tree master is one sided, add other to right
        if tree_master.left is None:
            tree_master.left = tree_master.right
        tree_master.right = tree_other
    else:
        # Tree master is full, add to lighter side
        if tree_master.left.total_fitness < tree_master.right.total_fitness:
            tree_master.left = add_to_tree(tree_master.left, tree_other)
        else:
            tree_master.right = add_to_tree(tree_master.right, tree_other)
    tree_master.calibrate_totals()
    return tree_master



