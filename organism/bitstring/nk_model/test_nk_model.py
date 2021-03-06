from unittest import TestCase as TC
import nk_model
from nk_model import *
from ..bitstring import Bitstring


class TestSimpleNKModel(TC):
    def test_init(self):
        dep = [[0, 1], [1, 0]]
        clt = [{0: 1, 1: 2, 2: 3, 3: 4}, {0: 5, 1: 6, 2: 7, 3: 8}]
        model = NKModelSimple(dep, clt)
        self.assertEqual(dep, model.dependency_lists)
        self.assertEqual(clt, model.contribution_lookup_tables)

    def test_calculate_fitness_hard(self):
        dep = [[0, 1], [1, 0], [2, 1]]
        clt = [{0: .1, 1: .2, 2: .3, 3: .4},
               {0: .5, 1: .6, 2: .7, 3: .8},
               {0: .9, 1: 1.0, 2: .15, 3: .25}]
        model = NKModelSimple(dep, clt)
        bs = Bitstring("010")
        expected_fitness = (.3 + .6 + .15) / 3.0
        self.assertAlmostEqual(expected_fitness, model.calculate_fitness(bs))

    def test_calculate_fitness_easy(self):
        model = NKModelSimple([[0], [1]], [{0: .2, 1: .3}, {0: .6, 1: .7}])
        bs = Bitstring("01")
        expected_fitness = (.3 + .6) / 2.0
        self.assertAlmostEqual(expected_fitness, model.calculate_fitness(bs))

    def test_calc_fit_lazy(self):
        dep = [[0], [1]]
        clt = [{}, {}]
        model = NKModelSimple(dep, clt)
        bs = Bitstring('01')
        bs2 = Bitstring('01')
        bs3 = Bitstring('10')
        self.assertNotEqual(model.calculate_fitness(bs), None)
        self.assertEqual(model.calculate_fitness(bs),
                         model.calculate_fitness(bs2))
        self.assertNotEqual(model.calculate_fitness(bs),
                            model.calculate_fitness(bs3))


class TestNKModelFactory(TC):
    def setUp(self):
        self.factory = NKModelFactory()

    def test_no_dependencies(self):
        smooth_nk = self.factory.no_dependencies(2)
        self.assertEqual(smooth_nk.dependency_lists, [[0], [1]])
        self.assertEqual(len(smooth_nk.contribution_lookup_tables), 2)
        smooth_nk.calculate_fitness(Bitstring("0"))
        self.assertEqual(len(smooth_nk.contribution_lookup_tables[0]), 1)
        self.assertEqual(len(smooth_nk.contribution_lookup_tables[1]), 0)

    def test_model_with_uniform_contribution_lookup_table(self):
        dep_lists = [[0, 1], [1, 2, 0], [2]]
        model = self.factory._model_with_uniform_contribution_lookup_table(
            dep_lists)
        clt = model.contribution_lookup_tables
        model.calculate_fitness(Bitstring("001"))
        self.assertEqual(len(clt), 3)
        self.assertEqual(len(clt[0]), 1)
        self.assertEqual(len(clt[1]), 1)
        self.assertEqual(len(clt[2]), 1)

    def test_max_depandancies(self):
        model = self.factory.max_dependencies(6)
        deps = model.dependency_lists
        self.assertEqual(6, len(deps))
        self.assertEqual(deps[0], list(range(6)))
        self.assertEqual(deps[-1], [5, 0, 1, 2, 3, 4])

    def test_consecutive_dependencies(self):
        model = self.factory.consecutive_dependencies(6, 2)
        deps = model.dependency_lists
        self.assertEqual(6, len(deps))
        self.assertEqual(deps[0], list(range(3)))
        self.assertEqual(deps[-1], [5, 0, 1])

    def test_non_consecutive_dependencies(self):
        model = self.factory.non_consecutive_dependencies(6, 2)
        deps = model.dependency_lists
        self.assertEqual(6, len(deps))
        self.assertEqual(len(deps[0]), 3)
        self.assertEqual(deps[0][0], 0)
        self.assertEqual(len(deps[-1]), 3)
        self.assertEqual(deps[-1][0], 5)

    def test_consecutive_dependencies_multigene(self):
        model = self.factory.consecutive_dependencies_multigene(3, 4, 2, 5)
        deps = model.dependency_lists
        self.assertEqual(3 * 4, len(deps))
        self.assertEqual(deps[0], [0, 1, 2, 3, 6, 9])
        self.assertEqual(deps[-1], [11, 9, 10, 2, 5, 8])

    def test_non_consecutive_dependencies_multigene(self):
        model = self.factory.non_consecutive_dependencies_multigene(
            6, 3, 2, 10)
        deps = model.dependency_lists
        self.assertEqual(18, len(deps))
        len_of_deps_is_11 = [len(dep_list) == 11 for dep_list in deps]
        len_of_set_deps_is_11 = [len(set(dep_list)) == 11 for dep in deps]
        self.assertTrue(all(len_of_deps_is_11))
        self.assertTrue(all(len_of_set_deps_is_11))
