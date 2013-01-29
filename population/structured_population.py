"""
Very similar to the MetaPopulation, except that the subpopulations
are arranged in a grid and that migrations are limited
to the nearest four neighbors.
"""

import random
from population import Population
from meta_population import MetaPopulation
from neighborhood import nearest_4_neighbors_by_linear_position


class StructuredPopulation(MetaPopulation):
    def __init__(self, sub_populations, migration_rate,
                 proportion_of_pop_migrated, width, height):
        super(StructuredPopulation, self).__init__(sub_populations, migration_rate, proportion_of_pop_migrated)
        self.width = int(width)
        self.height = int(height)
        assert(self.width > 1)
        assert(self.height > 0)
        assert(self.height * self.width == len(self.list_of_populations))

    def migrate(self):
        """
        Perform migrations in population
        """
        number_migrating_pops = int(self.mig_rate *
                                    len(self.list_of_populations))

        source_pop_indices = random.sample(
                list(range(len(self.list_of_populations))),
                number_migrating_pops)

        for source_pop_index in source_pop_indices:
            neighbors = nearest_4_neighbors_by_linear_position(
                    self.width, self.height, source_pop_index)
            dest_pop_index = random.choice(neighbors)
            source_pop = self.list_of_populations[source_pop_index]
            dest_pop = self.list_of_populations[dest_pop_index]
            self.subpop_migrate(source_pop, dest_pop)
