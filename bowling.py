#!/usr/local/bin/python

class Game(object):

    def __init__(self):
        self.rolls = [0] * 23
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        score = 0
        for roll in self.rolls:
            score += roll
        return score
