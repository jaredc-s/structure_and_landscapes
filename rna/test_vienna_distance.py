from unittest import TestCase as TC
import vienna_distance


class TestModule(TC):
    module = vienna_distance

    def test_distance_unequal(self):
        distance = self.module.get_distance(
            "CGCAGGGAUACCCGCG", "GCGCCCAUAGGGACGC")
        self.assertGreater(distance, 0)

    def test_distance_same(self):
        distance = self.module.get_distance("CGAUGCC", "CGAUGCC")
        self.assertEqual(distance, 0)

    def test_get_tRNA_sequence(self):
        seq = self.module.get_tRNA_sequence()
        self.assertTrue(set(seq) <= set("ATCG"))

    def test_get_distance_from_tRNA_sequence(self):
        target = self.module.get_tRNA_sequence()
        distance_at_target = self.module.get_distance_from_tRNA_sequence(
            target)
        self.assertEqual(distance_at_target, 0)

    def test_fold(self):
        seq = "ACTGAAATTGACCCTGTTAAAACTCGCTCGCTAGCTAGCTC"
        struc = self.module.fold(seq)
        self.assertEqual(len(struc), len(seq))
