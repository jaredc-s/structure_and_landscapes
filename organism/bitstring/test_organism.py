from unittest import TestCase as TC
from bitstring import Bitstring
import organism
from organism import Organism
from ..test_abstract_organism import MixinTestOrganism, MixinTestModule


class TestModule(MixinTestModule, TC):
    organism = organism
    Organism = Organism

    def test_default_organism(self):
        org = self.organism.default_organism
        self.assertAlmostEqual(org.fitness, 1)

    def test_random_organism(self):
        org = self.organism.random_organism(8)
        org.fitness


class TestOrganism(MixinTestOrganism, TC):
    Organism = Organism

    def setUp(self):
        self.value_0 = Bitstring("000")
        self.value_1 = Bitstring("001")
        self.value_2 = Bitstring("111")

    def test_init_exception(self):
        with self.assertRaises(ValueError):
            self.Organism("000")

    def test_fitness(self):
        g0 = self.Organism(self.value_0)
        self.assertAlmostEqual(1, g0.fitness)
        g1 = self.Organism(self.value_1)
        self.assertAlmostEqual(2, g1.fitness)
