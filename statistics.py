from numpy import mean


class StatisticsService(object):
    def __init__(self, classification=None, guesses=None):
        self.classification = classification
        self.guesses = guesses
        self.classes = set(classification)

    def precision(self, cls):
        all_positives = len([x for x in self.guesses if x == cls])
        if all_positives == 0:
            return 0
        true_positives = len([x for i, x in enumerate(self.guesses) if x == cls and self.classification[i] == cls])
        return float(true_positives) / float(all_positives)

    def average_precision(self):
        return mean([self.precision(cls) for cls in self.classes])

    def recall(self, cls):
        true_positives = len([x for i, x in enumerate(self.guesses) if x == cls and self.classification[i] == x])
        return float(true_positives) / len([x for x in self.classification if x == cls])

    def average_recall(self):
        return mean([self.recall(cls) for cls in self.classes])

    def f1(self):
        p = self.average_precision()
        r = self.average_recall()
        return 2 * p * r / (p + r)

    def accuracy(self):
        correct_guesses = len([x for i, x in enumerate(self.guesses) if self.classification[i] == x])
        return float(correct_guesses) / len(self.guesses)


if __name__ == '__main__':
    statistics = StatisticsService(classification=[1, 2, 1, 2, 1], guesses=[1, 1, 1, 2, 1])
    print statistics.average_precision()
    print statistics.average_recall()
    print statistics.f1()
    print statistics.accuracy()
