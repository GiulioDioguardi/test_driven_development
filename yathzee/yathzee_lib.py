#!/usr/bin/python

class YathzeeScoreCheckerError(Exception):
    pass

class YathzeeScoreChecker(object):

    def __init__(self, dices):
        self.dices = sorted(dices)
        self.check_length()
        self.check_type()
        self.check_range()

    def check_length(self):
        if len(self.dices) != 5:
            raise YathzeeScoreCheckerError(
                "Incorrect list length. Required 5, got %s" % (len(self.dices)))

    def check_type(self):
        if not all(isinstance(x, int) for x in self.dices):
            raise YathzeeScoreCheckerError(
                "List must only contain integers. Got %s" % (self.dices))
    def check_range(self):
        if any((x < 1 or x > 6) for x in self.dices):
            raise YathzeeScoreCheckerError(
                "Integer out of range. Must be between 1 and 6. "
                "Got %s" % (self.dices))

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

    def add_designated_values(self, value):
        score = 0
        for dice in self.dices:
            if dice == value:
                score += value
        return score

    def three_of_kind(self):
        return self.number_of_kind(3)

    def four_of_kind(self):
        seqs = []
        for i in range(2):
            seqs.append(self.dices[0 + i] == self.dices[1 + i] and \
                self.dices[0 + i] == self.dices[2 + i] and \
                self.dices[0 + i] == self.dices[3 + i])
        if any(seqs):
            return sum(self.dices)
        return 0

    def number_of_kind(self, number):
        seqs = []
        for i in range(6 - number):
            seqs.append(self.dices[0 + i] == self.dices[1 + i] and \
                self.dices[0 + i] == self.dices[2 + i])
        if any(seqs):
            return sum(self.dices)
        return 0

