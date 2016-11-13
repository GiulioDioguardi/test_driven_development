#!/usr/local/bin/python

import unittest
from bowling import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.g.score())

if __name__ == "__main__":
    unittest.main()
