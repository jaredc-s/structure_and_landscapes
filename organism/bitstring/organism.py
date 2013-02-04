"""
Organisms with genomes represented as bitstrings.

Immutable class.
"""
import random
import bitstring
from bitstring import Bitstring
from ..abstract_organism import AbstractOrganism


class Organism(AbstractOrganism):

    def __init__(self, *args, **kwargs):
        super(Organism, self).__init__(*args, **kwargs)
        if (isinstance(self, Organism) and
                not isinstance(self.value, Bitstring)):
            raise ValueError("Bitstring Organisms must hold Bitstrings")

    def _mutated_value(self):
        """
        the mutate method of an organism calls the module
        mutate and returns a new organism with the mutation
        note: original organism is unchanged
        """
        return self.value.single_step_mutant()

    def _evaluate_fitness(self):
        """
        fitness of this organism is the hamming distance of
        its bitstring from a bitstring composed of all False's
        """
        return 1 + sum(self.value)


default_organism = Organism(Bitstring(False for _ in range(10)))


def random_organism(length):
    bits = [True, False]
    sequence = [random.choice(bits) for _ in range(length)]
    bs = Bitstring(sequence)
    return Organism(bs)
