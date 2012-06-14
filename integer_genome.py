"""
Simple representation of a genome.

Intended for testing purposes.
"""


class Genome(object):
    def __init__(self, value):
        assert(isinstance(value, int))
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.value)

default_genome = Genome(0)
