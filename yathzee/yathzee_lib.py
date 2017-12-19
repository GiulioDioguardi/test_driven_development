#!/usr/bin/python

class YathzeeScoreCheckerError(Exception):
    pass

class YathzeeScoreChecker(object):

    def __init__(self, dices):
        self.dices = dices
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
        return self.number_of_kind(3, sum(self.dices))

    def four_of_kind(self):
        return self.number_of_kind(4, sum(self.dices))

    def yathzee(self):
        return self.number_of_kind(5, 50)

    def number_of_kind(self, number, score):
        if self.most_of_the_same() > number:
            return score
        return 0

    def most_of_the_same(self):
        most_same = 0
        for dice in self.dices:
            current_dice = dice
            current_same = 1
            for checked_dice in self.dices:
                if checked_dice == current_dice:
                    current_same += 1
            most_same = max(most_same, current_same)
        return most_same

    def small_straight(self):
        if self.longest_consecutive() > 3:
            return 30
        return 0

    def large_straight(self):
        if self.longest_consecutive() > 4:
            return 40
        return 0

    def longest_consecutive(self):
        longest_streak = 0
        for num in self.dices:
            current_num = num
            current_streak = 1
            while current_num + 1 in self.dices:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak

    def chance(self):
        return sum(self.dices)
