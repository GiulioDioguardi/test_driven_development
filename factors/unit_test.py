#!/usr/bin/python

import unittest
from factors import factors_of

class TestFactors(unittest.TestCase):

    def test_factors(self):
        self.assertEquals([], factors_of(1))
        self.assertEquals([2], factors_of(2))
        self.assertEquals([3], factors_of(3))
        self.assertEquals([2,2], factors_of(4))
        self.assertEquals([5], factors_of(5))
        self.assertEquals([2,3], factors_of(6))
        self.assertEquals([7], factors_of(7))
        self.assertEquals([2,2,2], factors_of(8))
        self.assertEquals([3,3], factors_of(9))
        self.assertEquals([2,3,5,11,11,13,17], factors_of(2*3*5*11*11*13*17))

if __name__ == "__main__":
    unittest.main()
