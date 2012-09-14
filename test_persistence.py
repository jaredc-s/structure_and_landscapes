from unittest import TestCase as TC
import persistence
class TestModule(TC):
    def test_save_load(self):
        filename = "test.shelf"
        key = "test_key"
        value = [42]
        persistence.save(filename, key, value)
        result = persistence.load(filename, key)
        self.assertEqual(value, result)
