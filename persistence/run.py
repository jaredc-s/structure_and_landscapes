"""
This module contains a class (Run) that encapsulate the
parameters and results of a single evolutionary simulation.
"""
import persistence
import copy


class Run(object):

    def __init__(self, initial_population, parameters, shelf_filepath):
        self.initial_population = initial_population
        self.parameters = parameters
        self.shelf_filepath = shelf_filepath

    def run(self):
        generations = self.parameters["generations"]
        pop = self.initial_population
        for gen in range(generations):
            pop.advance_generation()
        self.final_population = copy.deepcopy(pop)
        persistence.save_with_unique_key(self.shelf_filepath, self)
