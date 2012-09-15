from unittest import TestCase as TC
import persistence
import tempfile
import os.path
import shutil

class TestModule(TC):

    def test_save_load(self):
        temp_dir = tempfile.mkdtemp()
        filename = "test.shelf"
        filepath = os.path.join(temp_dir, filename)
        key = "test_key"
        value = [42]
        persistence.save(filepath, key, value)
        result = persistence.load(filepath, key)
        self.assertEqual(value, result)
        shutil.rmtree(temp_dir)
