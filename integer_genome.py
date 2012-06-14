"""
Simple representation of a genome.

Intended for testing purposes.
"""


class Genome(object):
    def __init__(self, value):
        assert(isinstance(value, int))
        self.value = value

default_genome = Genome(0)
