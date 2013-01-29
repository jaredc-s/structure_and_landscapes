"""
Meant to hold a population of organisms
Should be robust enough to handle bitstrings, user-defined alphabet etc.
Updates should:
1. replicate organisms
2. Calculate fitness for all organisms
"""

import random
from structure_and_landscapes.utility import selection


class Population(object):
    def __init__(self, init_pop, mutation_rate=1.0, carrying_capacity=None):
        self.population = list(init_pop)
        if carrying_capacity is None:
            self.carrying_capacity = len(self.population)
        else:
            self.carrying_capacity = carrying_capacity
        self.mutation_rate = mutation_rate

    def __iter__(self):
        return iter(self.population)

    def __len__(self):
        return len(self.population)

    def __getitem__(self, key):
        return self.population[key]

    def __setitem__(self, key, item):
        self.population[key] = item

    def is_full(self):
        return len(self.population) == self.carrying_capacity

    def replicate(self):
        """
        Creates one mutant for every member of the population
        and adds them to the population
        """
        mutants = [org.mutate() for org in self.population]
        self.population += mutants

    def remove_at_random(self):
        """
        Currently removes organisms from population at random
        in the future should look at a way to evaluate fitness
        and cull based off that
        """
        if len(self.population) > self.carrying_capacity:
            self.population = [random.choice(self.population)
                               for i in range(self.carrying_capacity)]

    def remove_least_fit(self):
        """
        Need to find way to choose based off of weighing the fitness values
        then can remove the sorting of tuples
        """
        self.population = selection.select(self.population,
                                           self.carrying_capacity)

    def moran_selection(self):
        self.population = selection.moran_death_birth(
            self.population, mutation_rate=self.mutation_rate,
            desired_number_of_orgs=self.carrying_capacity)

    def advance_generation(self):
        self.moran_selection()

    def add_to_pop(self, org):
        self.population.append(org)

    def max_fitness(self):
        return max([org.fitness for org in self.population])

    def mean_fitness(self):
        fits = [org.fitness for org in self.population]
        return float(sum(fits)) / len(fits)
