from unittest import TestCase as TC
from nk_model import *
from random import Random
from bitstring import Bitstring


class TestNKModel(TC):
    def setUp(self):
        self.clt_smooth = [[.25, .75], [.4, .8]]
        self.smooth = NKModel(2, 0, self.clt_smooth)
        self.clt_rugged = [[.25, .75, .1, 0], [.4, .8, .6, .7]]
        self.rugged = NKModel(2, 1, self.clt_rugged)

    def test_init(self):
        nk = NKModel()
        self.assertEqual(nk.n, 2)
        self.assertEqual(nk.k, 0)
        nk2 = NKModel(4, 3)
        self.assertEqual(nk2.n, 4)
        self.assertEqual(nk2.k, 3)
        nk3 = NKModel(k=6, n=10)
        self.assertEqual(nk3.n, 10)
        self.assertEqual(nk3.k, 6)

    def test_init_table(self):
        self.assertEqual(
            self.smooth.contribution_lookup_table, self.clt_smooth)

    def test_determine_fitness(self):
        b = Bitstring("10")
        smooth_fit = self.smooth.determine_fitness(b)
        expected_smooth_fit = (.75 + .4) / 2
        self.assertEqual(smooth_fit, expected_smooth_fit)
        rugged_fit = self.rugged.determine_fitness(b)
        expected_rugged_fit = (.1 + .8) / 2
        self.assertEqual(rugged_fit, expected_rugged_fit)

    def test_determine_fitness_from_random(self):
        b = Bitstring("10")
        rug_fit = self.rugged.determine_fitness_from_random(b)
        expected_rugged_fit = (.1 + .8) / 2
        self.assertEqual(rug_fit, expected_rugged_fit)


class TestModule(TC):
    def test_generate_constribution_lookup_table(self):
        n, k = 10, 2
        clt = generate_contribution_lookup_table(n, k)
        self.assertEqual(len(clt), n)
        self.assertEqual(len(clt[0]), 2 ** (k + 1))
        self.assertEqual(len(clt[-1]), 2 ** (k + 1))

    def test_get_substring_with_wrapping(self):
        b = Bitstring("11100")
        sub1 = get_substring_with_wrapping(b, k=3, i=1)
        self.assertEqual(Bitstring("1100"), sub1)
        sub2 = get_substring_with_wrapping(b, k=3, i=2)
        self.assertEqual(Bitstring("1001"), sub2)
        sub3 = get_substring_with_wrapping(b, k=3, i=3)
        self.assertEqual(Bitstring("0011"), sub3)
        
    def test_deconstruct_bitstring(self):
        B = Bitstring
        b = B("11001")
        subs = deconstruct_bitstring(b, 3)
        expected = [B("1100"), B("1001"),
                    B("0011"), B("0111"),
                    B("1110")]
        self.assertEqual(subs, expected)
        
    def test_deconstruct_random(self):
        B = Bitstring
        b = Bitstring("100")
        l = determine_inner_dependencies(3,2)
        sub = decontruct_random_bitstring(b, l)
        self.assertEqual(3, len(sub))
        self.assertEqual(sub[0], B("100"))

    def test_inner_dependencies(self):
        l = determine_inner_dependencies(4, 2)
        self.assertEqual(len(l), 4)
        self.assertEqual(len(l[0]), 3)
        self.assertEqual(l[0][0], 0)

