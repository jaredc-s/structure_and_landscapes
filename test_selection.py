import unittest
from unittest import TestCase as TC

import selection
from selection import select

class MockRandom(object):
    def __init__(self,value):
        self.value = value
    
    def random(self):
        return self.value

class TestSelection(TC):
    def test_init(self):
        #pop = [5,6,3,2]
        #fit = [1,15,16,17]
        #num = 3
        #new=select(pop,fit,num)
        pass
        #self.assertItemsEqual([6,3,2],new)
