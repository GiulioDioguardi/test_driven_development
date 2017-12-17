#!/usr/bin/python

class YathzeeScoreCheckerError(Exception):
    pass

class YathzeeScoreChecker(object):

    def __init__(self, dices):
        self.dices = sorted(dices)
        if len(dices) != 5:
            raise YathzeeScoreCheckerError(
                "Incorrect list length. Required 5, got %s" % (len(dices)))
        if not all(isinstance(x, int) for x in dices):
            raise YathzeeScoreCheckerError(
                "List must only contain integers. Got %s" % (dices))
        self.check_range()

    def check_range(self):
        if any((x < 1 or x > 6) for x in self.dices):
            raise YathzeeScoreCheckerError(
                "Integer out of range. Must be between 1 and 6. "
                "Got %s" % (self.dices))

    def add_designated_values(self, value):
        score = 0
        for dice in self.dices:
            if dice == value:
                score += value
        return score

    def ones(self):
        return self.add_designated_values(1)

    def twos(self):
        return self.add_designated_values(2)

    def threes(self):
        return self.add_designated_values(3)

    def fours(self):
        return self.add_designated_values(4)

    def fives(self):
        return self.add_designated_values(5)

    def sixes(self):
        return self.add_designated_values(6)

