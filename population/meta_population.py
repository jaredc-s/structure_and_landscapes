"""
Meta populations have multple instantiations of
population class

Migration occurs generation by replicating organisms from
one subpopulation and overwriting the same amount in another

Migration rate is the proportion of subpopulations
experiencing a migration event

Proportion of population migrated is proportion of
population duplicated from the source subpopulation on top of the
destination subpopulation in each migration event

Migrations in the MetaPopulation are not localized, populations
have no spatial nearness.
"""

import random
import itertools
from structure_and_landscapes.utility.selection import select
from population import Population
from neighborhood import nearest_4_neighbors_by_linear_position


class MetaPopulation(object):
    def __init__(self, sub_populations, migration_rate,
                 proportion_of_pop_migrated):
        self.list_of_populations = list(sub_populations)
        self.mig_rate = migration_rate
        self.prop_miged = proportion_of_pop_migrated

    def __iter__(self):
        return iter(self.list_of_populations)

    def __getitem__(self, key):
        return self.list_of_populations[key]

    def __len__(self):
        return len(self.list_of_populations)

    def migrate(self):
        """
        Perform migrations in population
        """
        source_pops_indices = self._migrant_subpopulation_indices()
        dest_pops_indices = self._migrant_subpopulation_indices()
        for source_index, dest_index in zip(source_pops_indices, dest_pops_indices):
            self.subpop_migrate(self.list_of_populations[source_index],
                    self.list_of_populations[dest_index])

    def _migrants_in_subpop(self):
        """
        Returns an iterable of indices denoting the orgs that are migrating.
        """
        number_of_orgs_per_subpop = len(self.list_of_populations[0])
        number_migrating_orgs = int(self.prop_miged * number_of_orgs_per_subpop)
        return random.sample(range(number_of_orgs_per_subpop), number_migrating_orgs)

    def subpop_migrate(self, source, dest):
        """
        Performs a migration (between two subpopulations)
        from source to dest
        """
        source_indices = self._migrants_in_subpop()
        dest_indices = self._migrants_in_subpop()
        for source_index, dest_index in zip(source_indices, dest_indices):
            dest[dest_index] = source[source_index]

    def _migrant_subpopulation_indices(self):
        """
        Returns a iterable of indicies for the subpopulation sampled from
        the subpopulations in proportion to the migration rate.
        """
        number_migrating_pops = int(
            self.mig_rate * len(self.list_of_populations))
        return random.sample(range(len(self.list_of_populations)), number_migrating_pops)

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


class StructuredPopulation(MetaPopulation):
    """
    Very similar to the MetaPopulation, except that the subpopulations
    are arranged in a grid and that migrations are limited
    to the nearest four neighbors.
    """
    def __init__(self, sub_populations, migration_rate,
                 proportion_of_pop_migrated, width, height):
        super(StructuredPopulation, self).__init__(
            sub_populations, migration_rate, proportion_of_pop_migrated)
        self.width = int(width)
        self.height = int(height)
        assert(self.width > 1)
        assert(self.height > 0)
        assert(self.height * self.width == len(self.list_of_populations))

    def migrate(self):
        """
        Perform migrations in population
        """
        source_pop_indices = self._migrant_subpopulation_indices()
        for source_pop_index in source_pop_indices:
            neighbors = nearest_4_neighbors_by_linear_position(
                self.width, self.height, source_pop_index)
            dest_pop_index = random.choice(neighbors)
            source_pop = self.list_of_populations[source_pop_index]
            dest_pop = self.list_of_populations[dest_pop_index]
            self.subpop_migrate(source_pop, dest_pop)


class ReservoirPopulation(MetaPopulation):
    """
    Instead of migrations occuring directly between two subpopulations,
    a proportion of each population is taken to a global reservoir,
    mixed, and equally distributed to the subpopulations.
    Migration rate is the proportion of subpopulations participating
    in the migration event (usually 1).
    """
    def migrate(self):
        subpop_indices = self._migrant_subpopulation_indices()
        subpop_index_to_migrant_indices = {
            subpop_index: self._migrants_in_subpop() for subpop_index in
            subpop_indices}
        lists_of_migrants = [
            [self.list_of_populations[subpop_index][migrant_index]
            for migrant_index in migrant_indices]
            for subpop_index, migrant_indices in subpop_index_to_migrant_indices.items()]
        migrants = list(itertools.chain.from_iterable(lists_of_migrants))
        random.shuffle(migrants)
        for subpop_index, migrant_indices in subpop_index_to_migrant_indices.items():
            for migrant_index in migrant_indices:
                self.list_of_populations[subpop_index][migrant_index] = migrants.pop()
