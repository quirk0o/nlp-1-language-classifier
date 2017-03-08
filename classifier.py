from lvector import LVec
from ngrams import *


def calculate_average_vector(n, texts):
    all_ngrams = [generate_ngrams(n, text) for text in texts]
    vectors = [LVec(ngrams=ngrams, n=n) for ngrams in all_ngrams]
    [vec.calculate_vector() for vec in vectors]
    vector = sum(vectors, LVec()) / len(texts)
    return vector
