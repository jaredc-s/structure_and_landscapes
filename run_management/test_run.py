from unittest import TestCase as TC
import tempfile
import os
import shutil

from structure_and_landscapes.organism.integer.organism \
    import Organism as int_organism
from structure_and_landscapes.population.population import Population

import run
import persistence


class TestRun(TC):
    def setUp(self):
        """
        Generates a temp file path.
        """
        temp_dir = tempfile.mkdtemp()
        filename = "test.shelf"
        filepath = os.path.join(temp_dir, filename)
        self.temp_file = filepath
        org_list = [int_organism(i) for i in range(1, 11)]
        self.init_pop = Population(org_list)

    def tearDown(self):
        """
        Closes temp file.
        """
        temp_dir = os.path.dirname(self.temp_file)
        shutil.rmtree(temp_dir)

    def test_run_simple(self):
        final_population = None
        other_data = "hi"
        r = run.Run(self.init_pop, final_population, {},
                    self.temp_file, other_data)
        with persistence.get_shelf(self.temp_file) as shelf:
            r_saved = shelf.values()[0]
            self.assertEquals(r_saved.final_population, None)
            self.assertEquals(r_saved.other_data, "hi")

    def test_run_population(self):
        run.run_population(self.init_pop, 5)

    def test_process_initial_org(self):
        rna = {'Organism Type': 'RNA'}
        bitstring = {'Organism Type': 'Bitstring', 'Length of Org': '5'}
        nk = {
            'Organism Type': 'NK Model',
            'Length of Org': '5',
            'K-total': '3'}
        nk_genes = {
            'Organism Type': 'NK Model',
            'Length of Org': '6',
            'Length of Gene': '2',
            'K-total': '3',
            'Number of Genes': '3',
            'K-intra': 1}
        run.process_initial_org(rna)
        run.process_initial_org(bitstring)
        run.process_initial_org(nk)
        run.process_initial_org(nk_genes)

        with self.assertRaises(run.OrgException):
            run.process_initial_org({'Organism Type': 'Wrong'})

    def test_process_initial_population(self):
        single_pop = {
            'Organism Type': 'Bitstring',
            'Mutation Rate': '0.01',
            'Length of Org': '5',
            'Orgs per Population': '10'}
        meta_pops = {
            'Number of Populations': '2',
            'Migration Rate': '0.33',
            'Proportion of Population Migrated': '1.0'}
        structured_pops = {
            'Number of Subpopulations in Width': '3',
            'Number of Subpopulations in Height': '4',
            'Migration Type': 'Local'}
        meta_pops.update(single_pop)
        structured_pops.update(meta_pops)
        run.process_initial_population(single_pop)
        run.process_initial_population(meta_pops)
        run.process_initial_population(structured_pops)

    def test_process_and_run(self):
        settings = {
            'Organism Type': 'Bitstring',
            'Mutation Rate': '0.01',
            'Length of Org': '5',
            'Number of Populations': '1',
            'Orgs per Population': '10',
            'Number of Generations': '2',
            'Output File Path': self.temp_file}
        run.process_and_run(settings)
