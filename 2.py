import os
import pickle
import sys
import json
from classifier import *
from ngram_builder import build_language_vector

CONFIG_FILE = 'samples.json'

if __name__ == '__main__':
    with open(CONFIG_FILE) as config:
        languages = json.load(config)

    n = int(sys.argv[1])

    print 'Building language data...'

    for language, data in languages.items():
        cache_file = 'cache/{}{}.data'.format(language.lower(), n)
        if os.path.exists(cache_file):
            with open(cache_file) as cache:
                data['vec'] = LVec(vec=pickle.load(cache))
        else:
            vec = build_language_vector(n, data['samples'])
            data['vec'] = vec

            # with open(cache_file, 'wb') as cache:
            #     pickle.dump(vec.vec, cache)

    classifier = LanguageClassifier(n, languages)

    while True:
        print classifier.determine_language(raw_input('> '))
