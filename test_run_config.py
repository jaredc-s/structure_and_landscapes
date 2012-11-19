from unittest import TestCase as TC
import run_config

class TestModule(TC):

    def test_dictionary_product(self):
        settings = {'A':[1, 2, 3],
                'B':['a', 'b'], 'C':[True,False]}
        expected_results_0 = {'A':1, 'B':'a', 'C':True}
        expected_results_1 = {'A':1, 'B':'a', 'C':False}
        expected_results_11 = {'A':3,'B':'b', 'C':False}
        results = run_config.dictionary_product(settings)
        self.assertEqual(len(results), 12)
        self.assertIn(expected_results_0, results)
        self.assertIn(expected_results_1, results)
        self.assertIn(expected_results_11, results)
