"""
Organisms with genomes represented as bitstrings.

Immutable class.
"""
import random
from mutate import mutate_value
import bitstring
from bitstring import Bitstring


class Organism(object):
    def __init__(self, value):
        """
        init takes a single argument which should be a bit string
        """
        assert(isinstance(value, Bitstring))
        self.value = value

    def __eq__(self, other):
        """
        organisms are equal if they have the same type
        and have the same bitstring
        """
        if not isinstance(other, type(self)):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        """
        organisms are hashable
        """
        return hash(self.value)

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

default_organism = Organism(Bitstring(False for _ in range(10)))
