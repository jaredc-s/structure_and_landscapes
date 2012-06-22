"""
Organisms with genomes represented as bitstrings.

Immutable class.
"""
import random
from mutate import mutate_value
import bitstring
from bitstring import Bitstring
import mixins


class Organism(mixins.KeyedHashingMixin):
    def __init__(self, value):
        """
        init takes a single argument which should be a bit string
        """
        self.value = value

    def mutate(self):
        """
        the mutate method of an organism calls the module
        mutate and returns a new organism with the mutation
        note: original organism is unchanged
        """
        mutated_value = mutate_value(self.value)
        return Organism(mutated_value)

    @property
    def fitness(self):
        """
        fitness of this organism is the hamming distance of
        its bitstring from a bitstring composed of all False's
        """
        return sum(self.value)

    def __key__(self):
        """
        Returns an object capable of being hashed and equaled
        """
        return self.value

default_organism = Organism(Bitstring(False for _ in range(10)))
