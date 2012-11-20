from unittest import TestCase as TC
import tempfile
import os
import shutil

from structure_and_landscapes.integer.integer_organism \
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

    def tearDown(self):
        """
        Closes temp file.
        """
        temp_dir = os.path.dirname(self.temp_file)
        shutil.rmtree(temp_dir)

    def test_run_simple(self):
        org_list = [int_organism(i) for i in range(1, 11)]
        init_pop = Population(org_list)
        final_population = None
        other_data = "hi"
        r = run.Run(init_pop, final_population, {},
                    self.temp_file, other_data)
        with persistence.get_shelf(self.temp_file) as shelf:
            r_saved = shelf.values()[0]
            self.assertEquals(r_saved.final_population, None)
            self.assertEquals(r_saved.other_data, "hi")
