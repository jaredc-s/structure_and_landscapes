"""
This module contains a class (Run) that encapsulate the
parameters and results of a single evolutionary simulation.
"""
import persistence


class Run(object):

    def __init__(self, initial_population, parameters, shelf_filepath):
        self.initial_population = initial_population
        self.parameters = parameters
        self.shelf_filepath = shelf_filepath

    def run(self):
        self.results = None
        persistence.save_with_unique_key(self, self.shelf_filepath)
