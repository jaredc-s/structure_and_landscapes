"""
Simple representation of a organism.

Intended for testing purposes.
"""
import random
from structure_and_landscapes.utility.mixins import KeyedHashingMixin
from ..abstract_organism import AbstractOrganism


class Organism(AbstractOrganism):

    def __init__(self, *args):
        value = args[0]
        assert(type(value) == int)
        super(Organism, self).__init__(*args)

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

    def _evaluate_fitness(self):
        return float(abs(self.value))


default_organism = Organism(0)
