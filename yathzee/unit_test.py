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

    def test_not_ints_in_list(self):
        try:
            self.create_score_checker([1,2,3,"four","five"])
            self.fail("Expected error has not occurred")
        except YathzeeScoreCheckerError as ex:
            check_for_message(self, ex, "List must only contain integers")

    def test_ints_are_out_of_range_too_low(self):
        try:
            self.create_score_checker([0,1,2,3,4])
            self.fail("Expected error has not occurred")
        except YathzeeScoreCheckerError as ex:
            check_for_message(self, ex, "Integer out of range")

    def test_ones_one_present(self):
        score_checker = self.create_score_checker([1,5,6,3,4])
        self.assertEquals(1, score_checker.ones())

    def test_ones_two_present(self):
        score_checker = self.create_score_checker([1,5,6,1,4])
        self.assertEquals(2, score_checker.ones())

    def test_twos_one_present(self):
        score_checker = self.create_score_checker([1,2,6,1,4])
        self.assertEquals(2, score_checker.twos())

    def test_threes_three_present(self):
        score_checker = self.create_score_checker([3,2,3,1,3])
        self.assertEquals(9, score_checker.threes())

    def test_fours_two_present(self):
        score_checker = self.create_score_checker([3,4,4,1,3])
        self.assertEquals(8, score_checker.fours())

    def test_fives_four_present(self):
        score_checker = self.create_score_checker([5,5,6,5,5])
        self.assertEquals(20, score_checker.fives())

    def test_sixes_two_present(self):
        score_checker = self.create_score_checker([6,5,6,5,3])
        self.assertEquals(12, score_checker.sixes())

if __name__ == "__main__":
    unittest.main()
