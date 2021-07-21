#!/usr/bin/python

import unittest
from factors import factors_of

class TestFactors(unittest.TestCase):

    def test_factors(self):
        self.assertEqual([], factors_of(1))
        self.assertEqual([2], factors_of(2))
        self.assertEqual([3], factors_of(3))
        self.assertEqual([2,2], factors_of(4))
        self.assertEqual([5], factors_of(5))
        self.assertEqual([2,3], factors_of(6))
        self.assertEqual([7], factors_of(7))
        self.assertEqual([2,2,2], factors_of(8))
        self.assertEqual([3,3], factors_of(9))
        self.assertEqual([2,3,5,11,11,13,17], factors_of(2*3*5*11*11*13*17))

if __name__ == "__main__":
    unittest.main()
