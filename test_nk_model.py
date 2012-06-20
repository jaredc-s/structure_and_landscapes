from unittest import TestCase as TC
from nk_model import NKModel
from random import Random


class TestNKModel(TC):
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
        clt = [[.25, .75], [.4, .8]]
        nk = NKModel(2, 0, clt)
        self.assertEqual(nk.contribution_lookup_table, clt)
