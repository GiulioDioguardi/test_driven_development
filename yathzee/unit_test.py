#!/usr/bin/python

import unittest
from yathzee_lib import YathzeeScoreChecker
from yathzee_lib import YathzeeScoreCheckerError

def check_for_message(test_func, exc, msg):
    test_func.assertTrue(msg in str(exc), "Incorrect message. Must contain "
        "[%s] ; I got [%s]" % (msg, exc))

class TestYathzeeScoreCheker(unittest.TestCase):

    def create_score_checker(self, dices):
        return YathzeeScoreChecker(dices)

    def test_equals_5(self):
        self.create_score_checker([1,2,3,4,5])

    def test_not_equals_5(self):
        try:
            self.create_score_checker([1,2,3,4])
            self.fail("Expected error has not occurred")
        except YathzeeScoreCheckerError as ex:
            check_for_message(self, ex, "Incorrect list length")

    def test_ones_one_present(self):
        score_checker = self.create_score_checker([1,5,6,3,4])
        self.assertEquals(1, score_checker.ones())

if __name__ == "__main__":
    unittest.main()
