import unittest
from unittest import TestCase as TC

import selection
from selection import select

class TestSelection(TC):
    def test_init(self):
        pop = [5,6,3,2]
        fit = [1,15,16,17]
        num = 3
        new=select(pop,fit,num)
        print new
        self.assertItemsEqual([6,3,2],new)
