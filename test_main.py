from nose.plugins.attrib import attr
from unittest import TestCase as TC
from main import *
from population.structure_population import Structured_Population
from population.population import Population
from integer.integer_organism import Organism


@attr('slow')
class TestModule(TC):
    def test_int_org_demo(self):
        int_org_demo()

    def test_nk_org_demo(self):
        nk_org_demo()

    def test_nk_gene_demo(self):
        nk_gene_demo()

    def test_nk_gene_structured_pop_demo(self):
        nk_gene_structured_pop_demo()

    def test_bit_org_demo(self):
        bit_org_demo()

    def test_rna_org_demo(self):
        rna_org_demo()

    def test_rna_org_structured_pop_demo(self):
        rna_org_structured_pop_demo()

    def test_structured_pop_demo(self):
        structured_pop_demo()

    def test_average_fitness_of_structured_population(self):
        int_org_1 = Organism(1)
        int_org_2 = Organism(2)
        pop_1 = Population([int_org_1 for _ in range(5)])
        pop_2 = Population([int_org_2 for _ in range(5)])
        struc_pop = Structured_Population([pop_1, pop_2], .5, .5)
        ave_fit = average_fitness_of_structured_population(struc_pop)
        self.assertAlmostEqual(1.5, ave_fit)
