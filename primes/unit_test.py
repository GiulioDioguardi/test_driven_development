#!/usr/bin/python

import unittest
import primes

class TestPrimes(unittest.TestCase):

    def assertcorrectprimes(self, number, expected):
        self.assertEqual(expected, primes.factortoprimes(number))

    def test_primes(self):
        self.assertcorrectprimes(None, [])

if __name__ == "__main__":
    unittest.main()
