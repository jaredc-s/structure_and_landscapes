from unittest import TestCase as TC
import vienna_distance


class TestModule(TC):

    def test_distance_unequal(self):
        distance = vienna_distance.get_distance(
            "CGCAGGGAUACCCGCG", "GCGCCCAUAGGGACGC")
        self.assertGreater(distance, 0)

    def test_distance_same(self):
        distance = vienna_distance.get_distance("CGAUGCC", "CGAUGCC")
        self.assertEqual(distance, 0)

    def test_get_tRNA_sequence(self):
        seq = vienna_distance.get_tRNA_sequence()
        self.assertTrue(set(seq) <= set("ATCG"))

    def test_get_distance_from_tRNA_sequence(self):
        target = vienna_distance.get_tRNA_sequence()
        distance_at_target = vienna_distance.get_distance_from_tRNA_sequence(
            target)
        self.assertEqual(distance_at_target, 0)

    def test_fold(self):
        seq = "ACTGAAATTGACCCTGTTAAAACTCGCTCGCTAGCTAGCTC"
        struc = vienna_distance.fold(seq)
        self.assertEqual(len(struc), len(seq))

