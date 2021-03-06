from unittest import TestCase as TC
import persistence
import tempfile
import os.path
import shutil
from contextlib import closing

from ..organism.integer import organism as org


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

    def test_load_not_found(self):
        with self.assertRaises(KeyError):
            bad_result = persistence.load(self.temp_file, "fake_key")

    def test_get_shelf(self):
        persistence.save(self.temp_file, "a", 1)
        persistence.save(self.temp_file, "b", 2)
        persistence.save(self.temp_file, "c", 3)
        with persistence.get_shelf(self.temp_file) as shelf:
            self.assertEqual(len(shelf), 3)

    def test_save_with_unique_key(self):
        for _ in range(10):
            persistence.save_with_unique_key(self.temp_file, None)
        with persistence.get_shelf(self.temp_file) as shelf:
            self.assertEqual(len(shelf), 10)

    def test_values(self):
        persistence.save(self.temp_file, "a", 1)
        persistence.save(self.temp_file, "b", 2)
        persistence.save(self.temp_file, "c", 3)

        stored_values = set(persistence.values(self.temp_file))
        self.assertEqual(len(stored_values), 3)
        self.assertEqual(set([1, 2, 3]), stored_values)

    def test_consolidate(self):
        path_1 = self.temp_file + "1"
        path_2 = self.temp_file + "2"
        path_3 = self.temp_file + "3"
        path_new = self.temp_file + "4"

        persistence.save(path_1, "a", 1)
        persistence.save(path_2, "b", 2)
        persistence.save(path_3, "c", 3)
        persistence.save(path_3, "d", 4)
        persistence.consolidate([path_1, path_2, path_3], path_new)

        stored_values = set(persistence.values(path_new))
        self.assertEqual(set([1, 2, 3, 4]), stored_values)
