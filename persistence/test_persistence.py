from unittest import TestCase as TC
import persistence
import tempfile
import os.path
import shutil
from contextlib import closing

import structure_and_landscapes.integer.integer_organism as org
class TestModule(TC):
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


    def test_save_load(self):
        key = "test_key"
        value = 42
        persistence.save(self.temp_file, key, value)
        result = persistence.load(self.temp_file, key)
        self.assertEqual(value, result)

    def test_save_load_org(self):
        key = "test_key"
        value = org.Organism(3)
        persistence.save(self.temp_file, key, value)
        result = persistence.load(self.temp_file, key)
        self.assertEqual(value, result)

    def test_get_shelf(self):
        persistence.save(self.temp_file, "a", 1)
        persistence.save(self.temp_file, "b", 2)
        persistence.save(self.temp_file, "c", 3)
        with closing(persistence.get_shelf(self.temp_file)) as shelf:
            self.assertEqual(len(shelf), 3)

    def test_save_with_unique_key(self):
        for _ in range(10):
            persistence.save_with_unique_key(self.temp_file, None)
        with closing(persistence.get_shelf(self.temp_file)) as shelf:
            self.assertEqual(len(shelf), 10)
