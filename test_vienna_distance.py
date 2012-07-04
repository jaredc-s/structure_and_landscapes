from unittest import TestCase as TC
import vienna_distance

class TestModule(TC):
    def test_distance_unequal(self):
        distance = vienna_distance.get_distance("CGCAGGGAUACCCGCG", "GCGCCCAUAGGGACGC")
        self.assertGreater(distance, 0)

    def test_distance_same(self):
        distance = vienna_distance.get_distance("CGAUGCC", "CGAUGCC")
        self.assertAlmostEqual(distance, 0, 3)

    def test_distance_uneven_length(self):
        seq_1 = "AAAAAAAAAAAAATTT"
        seq_2 = "CCCCCCCCCCcCCGGGCCCCC"
        distance = vienna_distance.get_distance(seq_1, seq_2)
        self.assertGreater(distance, 0)

if __name__ == "__main__":
    import unittest
    unittest.main()
