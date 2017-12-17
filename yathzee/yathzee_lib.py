#!/usr/bin/python

class YathzeeScoreChecker(object):

    def __init__(self, dices):
        self.dices = sorted(dices)

    def ones(self):
        score = 0
        for dice in self.dices:
            if dice == 1:
                score += 1
        return score
