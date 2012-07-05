from unittest import TestCase as TC
import vienna_distance

class TestModule(TC):
    def test_distance_unequal(self):
        distance = vienna_distance.get_distance("CGCAGGGAUACCCGCG", "GCGCCCAUAGGGACGC")
        self.assertGreater(distance, 0)

    def test_distance_same(self):
        distance =  vienna_distance.get_distance("CGAUGCC", "CGAUGCC")
        self.assertEqual(distance, 0)

    def test_get_tRNA_sequence(self):
        expected = "GCCTCGATAGCTCAGTTGGGAGAGCGTACGACTGAAGATCGTAAGGtCACCAGTTCGATCCTGGTTCGGGGCA"
        actual = vienna_distance.get_tRNA_sequence()
        self.assertEqual(expected, actual)

    def test_get_distance_from_tRNA_sequence(self):
        target = vienna_distance.get_tRNA_sequence()
        distance_at_target = vienna_distance.get_distance_from_tRNA_sequence(target)
        self.assertEqual(distance_at_target, 0)

    def test_fold(self):
        seq = "AAAAAAAAAUUUUUUUUU"
        struc = vienna_distance.fold(seq)
        self.assertEqual(len(struc), len(seq))
