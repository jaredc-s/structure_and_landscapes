from unittest import TestCase as TC

import integer_genome


class TestGenome(TC):
    pass

class TestModule(TC):
    def test_default_genome(self):
        genome = integer_genome.default_genome
