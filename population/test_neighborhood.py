from unittest import TestCase as TC
from neighborhood import *

class TestModule(TC):
    def setUp(self):
        self.grid_width = 4
        self.grid_height = 5

    def test_convert_linear_ordering_to_coordinate_pair(self):
        result_0 = convert_linear_ordering_to_coordinate_pair(3, 0)
        self.assertEqual(result_0, (0, 0))
        result_11 = convert_linear_ordering_to_coordinate_pair(3, 11)
        self.assertEqual(result_11, (2, 3))
        result_5 = convert_linear_ordering_to_coordinate_pair(3, 5)
        self.assertEqual(result_5, (2, 1))

    def test_convert_coordinate_pair_to_linear_ordering(self):
        result_0_0 = convert_coordinate_pair_to_linear_ordering(3, 0, 0)
        self.assertEqual(result_0_0, 0)
        result_2_3 = convert_coordinate_pair_to_linear_ordering(3, 2, 3)
        self.assertEqual(result_2_3, 11)
        result_2_1 = convert_coordinate_pair_to_linear_ordering(3, 2, 1)
        self.assertEqual(result_2_1, 5)

    def test_convert_inverse(self):
        for i in range(self.grid_width * self.grid_height):
            x, y = convert_linear_ordering_to_coordinate_pair(
                    self.grid_width, i)
            result = convert_coordinate_pair_to_linear_ordering(
                    self.grid_width, x, y)
            self.assertEqual(i, result)

    def test_correct_for_wrapping(self):
        result_0 = correct_for_wrapping(self.grid_width,
                self.grid_height, 2, 3)
        self.assertEqual(result_0, (2, 3))
        result_1 = correct_for_wrapping(self.grid_width,
                self.grid_height, 2, -1)
        self.assertEqual(result_1, (2, 4))
        result_2 = correct_for_wrapping(self.grid_width,
                self.grid_height, -2, -2)
        self.assertEqual(result_2, (2, 3))

    def test_nearest_4_neighbors(self):
        neighbors = nearest_4_neighbors(self.grid_width,
                self.grid_height, 0, 0)
        expected_neighbors = {(0, 4), (0, 1), (1, 0), (3, 0)}
        self.assertEqual(set(neighbors), expected_neighbors)

    def test_nearest_4_neighbors_by_linear_position(self):
        neighbors = nearest_4_neighbors_by_linear_position(self.grid_width,
                self.grid_height, 0)
        expected_neighbors = {16, 4, 1, 3}
        self.assertEqual(set(neighbors), expected_neighbors)

