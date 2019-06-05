#!/usr/bin/python

import unittest
import primes

class TestPrimes(unittest.TestCase):

    def assertcorrectprimes(self, number, expected):
        self.assertEqual(expected, primes.factortoprimes(number))

    def test_primes(self):
        self.assertcorrectprimes(None, [])
        self.assertcorrectprimes(1, [])
        self.assertcorrectprimes(2, [2])
        self.assertcorrectprimes(3, [3])
        self.assertcorrectprimes(4, [2,2])
        self.assertcorrectprimes(5, [5])
        self.assertcorrectprimes(6, [2,3])
        self.assertcorrectprimes(7, [7])
        self.assertcorrectprimes(8, [2,2,2])
        self.assertcorrectprimes(9, [3,3])
        self.assertcorrectprimes(3*13*23*31, [3,13,23,31])


if __name__ == "__main__":
    unittest.main()
