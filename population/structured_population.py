"""
Very similar to the MetaPopulation, except that the subpopulations
are arranged in a grid and that migrations are limited
to the nearest four neighbors.
"""

import random
from structure_and_landscapes.utility.selection import select
from population import Population
from meta_population import MetaPopulation


class StructuredPopulation(MetaPopulation):
    def __init__(self, sub_populations, migration_rate,
                 proportion_of_pop_migrated, height, width):
        super(StructuredPopulation, self).__init__(sub_populations, migration_rate, proportion_of_pop_migrated)
        self.height = int(height)
        self.width = int(width)
        assert(self.height > 0)
        assert(self.width > 1)
        assert(self.height * self.width == len(self.list_of_populations))

    def migrate(self):
        """
        Perform migrations in population
        """
        number_migrating_pops = int(self.mig_rate *
                                    len(self.list_of_populations))

        source_pops = random.sample(self.list_of_populations,
                                  number_migrating_pops)

        dest_pops = random.sample(self.list_of_populations,
                                  number_migrating_pops)
        for source, dest in zip(source_pops, dest_pops):
            self.subpop_migrate(source, dest)

