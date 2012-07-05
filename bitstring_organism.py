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
        self.f = None

    def mutate(self):
        """
        the mutate method of an organism calls the module
        mutate and returns a new organism with the mutation
        note: original organism is unchanged
        """
        return Organism(self._mutate_value())

    def _mutate_value(self):
        return mutate_value(self.value)

    @property
    def fitness(self):
        """
        fitness of this organism is the hamming distance of
        its bitstring from a bitstring composed of all False's
        """
        if self.f is None:
            self.f = sum(self.value)
        return self.f

    def __key__(self):
        """
        Returns an object capable of being hashed and equaled
        """
        return self.value

    def __repr__(self):
        """
        Organism(value=Bitstring('10101'))
        """
        return "{}(value={})".format(self.__class__.__name__, self.value)

default_organism = Organism(Bitstring(False for _ in range(10)))
