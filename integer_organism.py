"""
Simple representation of a organism.

Intended for testing purposes.

See bitstring_organism.py for more documentation.
"""
import random
from mutate import mutate_value
from mixins import KeyedHashingMixin


class Organism(KeyedHashingMixin):
    def __init__(self, value):
        assert(isinstance(value, int))
        self.value = value

    def mutate(self):
        mutated_value = mutate_value(self.value)
        return Organism(mutated_value)

    @property
    def fitness(self):
        return float(abs(self.value))

    def __key__(self):
        """
        Returns hashable object
        """
        return self.value

    def __repr__(self):
        """
        Looks like Organism(value=1)
        """
        return "{}(value={})".format(self.__class__.__name__, self.value)


default_organism = Organism(0)
