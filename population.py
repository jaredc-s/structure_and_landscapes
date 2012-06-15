"""
Meant to hold a population of organisms
Should be robust enough to handle bitstrings, user-defined alphabet etc.
Updates should:
1. replicate organisms
2. Calculate fitness for all organisms
"""

import random
import bitstring_organism
from selection import select


class Population(object):
    def __init__(self, init_pop, max_size=None):
        self.population = list(init_pop)
        self.size = len(self.population)
        if max_size is None:
            self.maxsize = len(self.population)

        else:
            self.maxsize = max_size
    
    def __iter__(self):
        return iter(self.population)

    def replicate(self):
        xmen = [org.mutate() for org in self.population]
        
        self.population += xmen
        self.size = len(self.population)

    def remove_at_random(self):
        """
        Currently removes organisms from population at random
        in the future should look at a way to evaluate fitness
        and cull based off that
        """
        if len(self.population) > self.maxsize:
            self.population = [random.choice(self.population)
                               for i in range(self.maxsize)]
            self.size = len(self.population)

    def remove_least_fit(self):
        """
        Need to find way to choose based off of weighing the fitness values
        then can remove the sorting of tuples
        """

        self.population = select(self.population, self.maxsize)
        self.size = len(self.population)

    def advance_generation(self):
        self.replicate()
        self.remove_least_fit()

default_population = Population([1, 1, 0, 0, 1])
