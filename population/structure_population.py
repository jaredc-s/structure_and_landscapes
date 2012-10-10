"""
Structured populations have multple instatiations of
population class

Migration occurs after each generation by swapping
between two subpopulations

Migration rate is equal to proption of subpopulations
experiencing a migration event

Proportion of population swapped is proportion of
population swapped in each migration event
"""

import random
from structure_and_landscapes.utility.selection import select
from population import Population


class Structured_Population(object):
    def __init__(self, sub_populations, migration_rate,
                 proportion_of_pop_swapped):
        self.list_of_populations = list(sub_populations)
        self.mig_rate = migration_rate
        self.prop_swapped = proportion_of_pop_swapped

    def __iter__(self):
        return iter(self.list_of_populations)

    def __getitem__(self, key):
        return self.list_of_populations[key]

    def __len__(self):
        return len(self.list_of_populations)

    def migrate(self):
        """should happen after replicate but
          before the culling
        However migration prior to replication would
          allow greater chance of survival
        """
        number_migrating_pops = int(self.mig_rate *
                                    len(self.list_of_populations))

        from_pops = random.sample(self.list_of_populations,
                                  number_migrating_pops)
        together = zip(from_pops[0::2], from_pops[1::2])
        for popA, popB in together:
            self.swap(popA, popB)

    def swap(self, popA, popB):
        number_migrating_orgs = int(self.prop_swapped * len(popA))
        popA_indices = random.sample(list(range(len(popA))),
                                     number_migrating_orgs)
        popB_indices = random.sample(list(range(len(popB))),
                                     number_migrating_orgs)
        for popA_index, popB_index in zip(popA_indices, popB_indices):
            (popA[popA_index], popB[popB_index]) = \
                (popB[popB_index], popA[popA_index])

    def replicate(self):
        for pop in self.list_of_populations:
            pop.replicate()

    def remove_at_random(self):
        """
        Currently removes organisms from population at random
        in the future should look at a way to evaluate fitness
        and cull based off that
        """
        for pop in self.list_of_populations:
            pop.remove_at_random()

    def moran_cull(self):
        for pop in self.list_of_populations:
            pop.moran_selection()

    def advance_generation(self):
        self.moran_cull()
        self.migrate()

    def max_fitness(self):
        return max([pop.max_fitness() for pop in self.list_of_populations])

    def mean_fitness(self):
        fits = [pop.mean_fitness() for pop in self.list_of_populations]
        return float(sum(fits)) / len(fits)
