from unittest import TestCase as TC
import mutate
import bitstring
import random
import bitstringLong

class TestModule(TC):

    def test_mutate_integer(self):
        value = 0
        mutated_value = mutate.mutate_value(value)
        self.assertNotEqual(value, mutated_value)

    def test_mutate_bitstring(self):
        value = bitstring.Bitstring("00")
        mutated_value = mutate.mutate_value(value)
        self.assertNotEqual(value, mutated_value)

    def test_mutate_bitLong(self):
        value = bitstringLong.Bitstring('1001')
        mutated_value = mutate.mutate_value(value)
        self.assertNotEqual(value, mutated_value)

    def test_mutate_value_raises(self):
        with self.assertRaises(TypeError):
            mutate.mutate_value({"hi", 2})

    def test_change_base(self):
        test_seq = "ACCGTA"
        sequence = mutate.mutate_value(test_seq)
        self.assertEqual(len(test_seq), len(sequence))
        self.assertNotEqual(test_seq, sequence)

    def test_change_base_many(self):
        test_seq = "AAAACCCCTTTTGGGG"
        for _ in range(100):
            test_seq = mutate.mutate_value(test_seq)
        self.assertTrue(set(test_seq) <= set("ATCG"))

    def test_mutation_rate(self):
        value = 0
        not_mutated_value = mutate.mutate_value(value, mutation_rate=-1.0)
        self.assertEqual(value, not_mutated_value)
        mutated_value = mutate.mutate_value(value, mutation_rate=1.0)
        self.assertNotEqual(value, mutated_value)
