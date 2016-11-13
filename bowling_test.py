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

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.g.score())

    def test_spare(self):
        self.g.roll(5)
        self.g.roll(5) #spare
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.g.score())

if __name__ == "__main__":
    unittest.main()
