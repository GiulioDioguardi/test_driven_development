#!/usr/local/bin/python

class Game(object):

    def __init__(self):
        self.rolls = [0] * 23
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def is_spare(self, findex):
        return self.rolls[findex] + self.rolls[findex + 1] == 10

    def is_strike(self, findex):
        return self.rolls[findex] == 10

    def strike_bonus(self, findex):
        return self.rolls[findex + 1] + self.rolls[findex + 2]

    def spare_bonus(self, findex):
        return self.rolls[findex + 2]

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index) 
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return score
