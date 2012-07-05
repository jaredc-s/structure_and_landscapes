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
        seq_1 = "AAAAAAAAAAAAATTTCCCCC"
        seq_2 = "CCCCCCCCCCcCCGGGCCCCC"
        distance = vienna_distance.get_distance(seq_1, seq_2)
        self.assertGreater(distance, 0)

    def test_distance_to_tRNA(self):
        seq_same = "GCCTCGATAGCTCAGTTGGGAGAGCGTACGACTGAAGATCGTAAGGtCACCAGTTCGATCCTGGTTCGGGGCA"
        seq_same = vienna_distance.get_tRNA_target()
        distance_to_same = vienna_distance.get_distance_from_tRNA(seq_same)
        self.assertAlmostEqual(distance_to_same, 0, 3)

        seq_different = "GCCTCGATAGCTCAGTTGGGAGAGCGTACGACTGAAGATCGTAAGGtCACCAGTTCGATCCTGGTTCGGGGCT"
        distance_to_different = vienna_distance.get_distance_from_tRNA(seq_different)
        self.assertGreater(distance_to_different, 0)

    def test_tRNA_target(self):
        expected = "GCCTCGATAGCTCAGTTGGGAGAGCGTACGACTGAAGATCGTAAGGtCACCAGTTCGATCCTGGTTCGGGGCA"
        self.assertEqual(vienna_distance.get_tRNA_target(), expected)
