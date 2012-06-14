"""
Meant to hold a population of organisms
Should be robust enough to handle bitstrings, user-defined alphabet etc.

Updates should:
1. replicate organisms
2. Calculate fitness for all organisms
"""

import random

class Population():
    def __init__(self,init_pop):
        self.population = list(init_pop)
        self.maxsize = len(self.population)
        
    def replicate(self):
        x-men = [organism.mutate() for org in self.population]
        self.population += x-men

    def remove_at_random(self):
        """
        Currently removes organisms from population at random
        in the future should look at a way to evaluate fitness and cull based off that
        """
        if self.population > self.maxsize:
            self.population = [random.choice(self.population) for i in range(self.maxsize)]

    def remove_least_fit(self):
        """
        Need to find way to choose based off of weighing the fitness values
        then can remove the sorting of tuples
        """
        fit_orgs = []
        for org in self.population:
            package = (org.eval_fitness(), org)
            fit_orgs.append(package)
        fit_orgs.sort()
        
        def select(population, fitness, num):
            total_fit = float(sum(fitness))
            rel_fitness = [f/total_fit for f in fitness]
            
            prob = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
            
            new_population = []
            for n in xrange(num):
                r = rand()
                for (i, individual) in enumerate(population):
                    if r<= prob[i]:
                        new_population.append(individual)
                        break
            return new_population

    def advance_generation(self):
        self.replicate()
        self.remove_least_fit()


