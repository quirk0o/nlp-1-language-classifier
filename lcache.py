import json
import os
import pickle

from collections import defaultdict

from lvector import LVec
from ngram_builder import build_language_vector

CONFIG_FILE = 'samples.json'


class LCache(object):
    def __init__(self, config=CONFIG_FILE):
        self.config = config
        self.languages = json.load(open(config))

    def build_language_vectors(self, n):
        for language, data in self.languages.items():
            cache_file = 'cache/{}{}.data'.format(language.lower(), n)
            if os.path.exists(cache_file):
                with open(cache_file) as cache:
                    data['vec'] = LVec(vec=defaultdict(lambda: 0.0, pickle.load(cache)))
            else:
                vec = build_language_vector(n, data['samples'])
                data['vec'] = vec

                with open(cache_file, 'wb') as cache:
                    pickle.dump(vec.vec.items(), cache)

        return self.languages
