"""
Simple representation of a organism.

Intended for testing purposes.
"""
import random
from mutate import mutate_value


class Organism(object):
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

    def mutate(self):
        mutated_value = mutate_value(self.value)
        return Organism(mutated_value)


default_organism = Organism(0)
