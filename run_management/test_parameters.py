from unittest import TestCase as TC
import parameters

class TestModule(TC):

    def test_dictionary_product(self):
        settings = {'A':[1, 2, 3],
                'B':['a', 'b'], 'C':[True,False]}
        expected_results_0 = {'A':1, 'B':'a', 'C':True}
        expected_results_1 = {'A':1, 'B':'a', 'C':False}
        expected_results_11 = {'A':3,'B':'b', 'C':False}
        results = parameters.dictionary_product(settings)
        self.assertEqual(len(results), 12)
        self.assertIn(expected_results_0, results)
        self.assertIn(expected_results_1, results)
        self.assertIn(expected_results_11, results)

    def test_split_lists_out(self):
        settings = {'A':"4",
                'B':"True",
                'C':["1", "2"]}
        without_lists, with_lists = parameters.split_lists_out(settings)
        self.assertIn('A', without_lists)
        self.assertIn('B', without_lists)
        self.assertIn('C', with_lists)

    def test_parse_contents_to_settings_dict_single(self):
        contents = "A:1\nB:2\nC:3"
        settings = parameters.parse_contents_to_settings_dict(contents)
        self.assertEqual({"A":"1", "B":"2", "C":"3"}, settings)

    def test_parse_contents_to_settings_dict_multiple(self):
        contents = "A:1,2\nB:3\nC:4,5"
        settings = parameters.parse_contents_to_settings_dict(contents)
        self.assertEqual({"A":["1", "2"], "B":"3", "C":["4", "5"]}, settings)

    def test_comments_whitespace_parseing(self):
        contents = """
        # Early comments

        Multiple words : 4, 5, 6 # End comment
        # After comments
        """
        settings = parameters.parse_contents_to_settings_dict(contents)
        self.assertEqual({"Multiple words":["4", "5", "6"]}, settings)

    def test_get_parameters_settings(self):
        contents = """
        A : 1
        B : 2, 3
        C : 4, 5
        """
        expected_start = {'A':'1', 'B':'2', 'C':'4'}
        expected_end = {'A':'1', 'B':'3', 'C':'5'}

        result = parameters.get_parameter_settings(contents)
        self.assertEqual(len(result), 4)
        self.assertIn(expected_start, result)
        self.assertIn(expected_end, result)

