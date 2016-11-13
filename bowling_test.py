#!/usr/local/bin/python

import unittest
from bowling import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_can_roll(self):
        self.g.roll()

    def test_gutter_game(self):
        pass

if __name__ == "__main__":
    unittest.main()
