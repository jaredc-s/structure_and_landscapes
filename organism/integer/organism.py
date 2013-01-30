"""
Simple representation of a organism.

Intended for testing purposes.
"""
import random
from ..abstract_organism import AbstractOrganism


class Organism(AbstractOrganism):

    def __init__(self, *args, **kwargs):
        super(Organism, self).__init__(*args, **kwargs)
        if not isinstance(self.value, int):
            raise ValueError("Integer Organisms must hold ints")

    def _mutated_value(self):
        """
        returns a int that is increment
        or decremented from the current state
        """
        if random.random() < 0.5:
            return self.value + 1
        else:
            return self.value - 1

    def _evaluate_fitness(self):
        return 1 + abs(self.value)


default_organism = Organism(0)
