import random
from test_meta_population import TestMetaPopulation
from structured_population import StructuredPopulation
from population import Population
from ..integer.integer_organism import Organism


class TestStructuredPopulation(TestMetaPopulation):
    def setUp(self):
        self.orgs = [Organism(1), Organism(2),
                     Organism(3), Organism(4)]

        self.pops = [Population(self.orgs) for _ in range(10)]
        self.metapop = StructuredPopulation(self.pops, 0.5, 0.5, 2, 5)
