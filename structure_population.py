import random
from selection import select
from population import Population
from selection import select

class Structured_Population(object):
    def __init__(self, sub_populations, maxsize = None):
        self.all_pop = list(sub_populations)

        if maxsize == None:
            self.max_size = maxsize
        else:
            self.max_size = len(sub_population[0])

    def __iter__(self):
        return iter(self.all_pop)

    def migrate(self, rate):
        """should happen after replicate but before the culling
        However migration prior to replication would allow greater chance of survival
        """

        from_pop = self.all_pop[random.randint(0, len(self.pop) - 1)]
        from_org = from_pop[random.randint(0, len(from_pop))]

        to_pop = self.all_pop[random.randint(0, len(self.pop) - 1)]

        if to_pop.is_full():
            to_org = to_pop[random.randint(0,len(to_pop))]
            self.pop[to_pop][to_org] = self.pop[from_pop][from_org]
        else:
            to_pop.add_to_pop(from_org)

        from_pop.remove_from_pop(from_org)

    def replicate(self):
        for pop in self.all_pop:
            pop.replicate()

    def remove_at_random(self):
        """
        Currently removes organisms from population at random
        in the future should look at a way to evaluate fitness
        and cull based off that
        """
        for pop in self.all_pop:
            pop.remove_at_random()

    def remove_least_fit(self):
        """
        Need to find way to choose based off of weighing the fitness values
        then can remove the sorting of tuples
        """
        for pop in self.all_pop:
            pop = select(pop, pop.maxsize)

    def advance_generation(self):
        self.replicate()
        self.remove_least_fit()
