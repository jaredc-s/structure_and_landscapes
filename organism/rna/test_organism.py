from unittest import TestCase as TC
import organism
from organism import Organism
from ..test_abstract_organism import MixinTestOrganism, MixinTestModule
import cmd_vienna_distance as vienna_distance

OPTIMAL_RNA_SEQUENCE = vienna_distance.get_tRNA_sequence()

class TestModule(MixinTestModule, TC):
    organism = organism
    Organism = Organism

    def test_default(self):
        def_org = self.organism.default_organism
        self.assertEqual(vienna_distance.get_tRNA_sequence(), def_org.value)

    def test_random_org(self):
        length_random_org = len(self.organism.random_organism().value)
        length_def_org = len(self.organism.default_organism.value)
        self.assertEqual(length_def_org, length_random_org)


class TestOrganism(MixinTestOrganism, TC):
    Organism = Organism

    def setUp(self):
        self.value_0 = OPTIMAL_RNA_SEQUENCE
        self.value_1 = "C" * len(OPTIMAL_RNA_SEQUENCE)
        self.value_2 = "C" * 10 + "G" * (len(OPTIMAL_RNA_SEQUENCE) - 10)

    def test_init_exception(self):
        with self.assertRaises(ValueError):
            self.Organism("AUXCG")

    def test_fitness(self):
        organism = self.Organism(self.value_0)
        all_As = "".join('A' for _ in organism.value)
        a_org = self.Organism(all_As)
        self.assertLess(a_org.fitness, organism.fitness)
