from collections import Counter, defaultdict
import math

MIN_OCCURENCES = 0.01


class LVec(object):
    def __init__(self, ngrams=None, n=None, vec=None):
        self.ngrams = ngrams
        self.counter = Counter(ngrams)
        self.n = n
        self.vec = vec or defaultdict(lambda: 0.0)

    def calculate_vector(self):
        n_factor = float(len(self.ngrams))
        for k in self.counter.keys():
            self.vec[k] = self.counter[k] / n_factor
        return self.vec

    def __add__(self, other):
        key_set = set()
        key_set.update(self.vec.keys())
        key_set.update(other.vec.keys())
        return LVec(
            vec=defaultdict(
                lambda: 0.0,
                {k: self.vec[k] + other.vec[k] for k in key_set}
            ),
            n=self.n
        )

    def __div__(self, divider):
        return LVec(
            vec=defaultdict(
                lambda: 0.0,
                {k: self.vec[k] / divider for k in self.vec.keys()}
            ),
            n=self.n
        )

    def len(self):
        return math.sqrt(sum([x ** 2 for x in self.vec.values()]))

    def __str__(self):
        common_items = filter(lambda (k, v): v > MIN_OCCURENCES, self.vec.items())
        other_items = filter(lambda (k, v): v <= MIN_OCCURENCES, self.vec.items())
        items_str = '\n'.join(['{}: {}'.format(k, v) for (k, v) in common_items])
        if len(other_items) > 0:
            return '{}\n... {} less common ngrams'.format(items_str, len(other_items))
        return items_str

    def cos_dist(self, other):
        key_set = set()
        key_set.update(self.vec.keys())
        key_set.update(other.vec.keys())
        numerator = sum([self.vec[k] * other.vec[k] for k in key_set])
        denominator = self.len() * other.len()
        if denominator == 0:
            return float('inf')
        return 1 - numerator / denominator
