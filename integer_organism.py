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
        """
        returns a int organism that is increment
        or decremented from the current state
        """
        new_value = self.value
        if random.random() < 0.5:
            new_value += 1
        else:
            new_value -= 1

        return Organism(new_value)

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
