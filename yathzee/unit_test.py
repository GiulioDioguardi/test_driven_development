#!/usr/bin/python

import unittest
from yathzee_lib import YathzeeScoreChecker

class TestYathzeeScoreCheker(unittest.TestCase):

    def create_score_checker(self, dices):
        return YathzeeScoreChecker(dices)

    def test_nothing(self):
        pass

    def test_ones_one_present(self):
        score_checker = self.create_score_checker([1,5,6,3,4])
        self.assertEquals(1, score_checker.ones())

if __name__ == "__main__":
    unittest.main()
