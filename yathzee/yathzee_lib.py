#!/usr/bin/python

class YathzeeScoreCheckerError(Exception):
    pass

class YathzeeScoreChecker(object):

    def __init__(self, dices):
        if len(dices) != 5:
            raise YathzeeScoreCheckerError(
                "Incorrect list length. Required 5, got %s" % (len(dices)))
        self.dices = sorted(dices)

    def ones(self):
        score = 0
        for dice in self.dices:
            if dice == 1:
                score += 1
        return score
