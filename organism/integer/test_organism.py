from unittest import TestCase as TC

import organism
from organism import Organism
from ..test_abstract_organism import MixinTestOrganism, MixinTestModule


class TestModule(MixinTestModule, TC):
    organism = organism
    Organism = Organism



class TestIntegerOrganism(MixinTestOrganism, TC):

    Organism = Organism

    def setUp(self):
        self.value_0 = 0
        self.value_1 = 1
        self.value_2 = 2

    def test_init_exception(self):
        with self.assertRaises(ValueError):
            self.Organism("1")

    def test_fitness(self):
        g0 = self.Organism(self.value_0)
        self.assertAlmostEqual(1, g0.fitness)
        g1 = self.Organism(self.value_1)
        self.assertAlmostEqual(2, g1.fitness)


