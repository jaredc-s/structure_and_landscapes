"""
Meant to hold a population of organisms
Should be robust enough to handle bitstrings, user-defined alphabet etc.

Updates should:
1. replicate organisms
2. Calculate fitness for all organisms
"""

import random

class Population(object):
    def __init__(self,init_pop,max_size=None):
        self.population = list(init_pop)
        self.size = len(self.population)
        if max_size == None:
            self.maxsize = len(self.population)
        
        else:
            self.maxsize = max_size
        
    def replicate(self):
        pass
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
        
        def select(population, fitness, num):
            total_fit = float(sum(fitness))
            rel_fitness = [f/total_fit for f in fitness]
            
            prob = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
            
            new_population = []
            for n in xrange(num):
                r = random.random()
                for (i, individual) in enumerate(population):
                    if r<= prob[i]:
                        new_population.append(individual)
                        break
            return new_population 

        fit_list = [org.eval_fit() for org in self.population]

        self.population = select(self.population, fit_list, self.maxsize)
        
    def advance_generation(self):
        self.replicate()
        self.remove_least_fit()

default_population = population([1,1,0,0,1])
