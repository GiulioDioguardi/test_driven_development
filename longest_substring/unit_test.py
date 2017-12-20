#!/usr/bin/python

import unittest
from longest_substring import length_of_longest_substring

class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring_1(self):
        self.assertEquals(1, length_of_longest_substring("bbbbb"))

    def test_can_get_longest_substring_3(self):
        string = "abcabcbb" #longest is 'abc'
        self.assertEquals(3, length_of_longest_substring(string))

    def test_can_cat_another_substring_3(self):
        self.assertEquals(3, length_of_longest_substring("pwwkew"))

    def test_acceptance(self):
        self.assertEquals(10, length_of_longest_substring(
            "asasdfwqoeriovaosidhpaosinasdonfvpasoidfnp"))

if __name__ == "__main__":
    unittest.main()
