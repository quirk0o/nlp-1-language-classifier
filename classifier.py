from lvector import LVec
from ngrams import *


class LanguageClassifier(object):
    def __init__(self, n, languages):
        self.languages = languages
        self.n = n

    def determine_language(self, input_text):
        ngrams = generate_ngrams(self.n, input_text)
        vec = LVec(n=self.n, ngrams=ngrams)
        vec.calculate_vector()
        distances = dict([(language, vec.cos_dist(data['vec'])) for language, data in self.languages.items()])

        return min(distances, key=distances.get)


def calculate_average_vector(n, texts):
    all_ngrams = [generate_ngrams(n, text) for text in texts]
    vectors = [LVec(ngrams=ngrams, n=n) for ngrams in all_ngrams]
    [vec.calculate_vector() for vec in vectors]
    vector = sum(vectors, LVec()) / len(texts)
    return vector
