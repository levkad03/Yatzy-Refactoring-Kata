from collections import Counter

POINTS_20 = 20
POINTS_15 = 15
POINTS_50 = 50
MIN_VAL = 1
MAX_VAL = 7


class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        total = d1 + d2 + d3 + d4 + d5
        return total

    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            for i, count in enumerate(counts):
                if i + 1 == die:
                    counts[i] += 1
        for count in counts:
            if count == 5:
                return POINTS_50
        return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum_points = 0
        for d in [d1, d2, d3, d4, d5]:
            if d == 1:
                sum_points += 1
        return sum_points

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum_points = 0
        for d in [d1, d2, d3, d4, d5]:
            if d == 2:
                sum_points += 2
        return sum_points

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        sum_points = 0
        for d in [d1, d2, d3, d4, d5]:
            if d == 3:
                sum_points += 3
        return sum_points

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        sum_points = 0
        for d in self.dice:
            if d == 4:
                sum_points += 4
        return sum_points

    def fives(self):
        sum_points = 0
        i = 0
        for d in self.dice:
            if d == 5:
                sum_points = sum_points + 5
        return sum_points

    def sixes(self):
        sum_points = 0
        for d in self.dice:
            if d == 6:
                sum_points = sum_points + 6
        return sum_points

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        for value in reversed(range(MIN_VAL, MAX_VAL)):
            if counts[value] == 2:
                return value * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        pairs = [value for value, count in counts.items() if count >= 2]
        if len(pairs) == 2:
            return sum(pairs) * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        for value, count in counts.items():
            if count >= 4:
                return value * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        for value, count in counts.items():
            if count >= 3:
                return value * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        comb1, comb2, comb3 = Yatzy.check_comb_for_small_straight(counts)
        if comb1 or comb2 or comb3:
            return POINTS_15
        return 0

    @staticmethod
    def check_comb_for_small_straight(counts):
        comb1 = all(i in counts for i in range(1, 5))
        comb2 = all(i in counts for i in range(2, 6))
        comb3 = all(i in counts for i in range(3, 7))
        return comb1, comb2, comb3

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = Counter([d1, d2, d3, d4, d5])
        first_combination, second_combination = Yatzy.check_combinations(tallies)
        if first_combination or second_combination:
            return POINTS_20
        return 0

    @staticmethod
    def check_combinations(tallies):
        first_combination = all(tallies[i] == 1 for i in range(1, 6))
        second_combination = all(tallies[i] == 1 for i in range(2, 7))
        return first_combination, second_combination

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = Counter([d1, d2, d3, d4, d5])
        if 3 in tallies.values() and 2 in tallies.values():
            pairs, threes = Yatzy.check_full_house(tallies)
            return pairs[0] * 2 + threes[0] * 3
        return 0

    @staticmethod
    def check_full_house(tallies):
        pairs = [key for key, val in tallies.items() if val == 2]
        threes = [key for key, val in tallies.items() if val == 3]
        return pairs, threes
