import json
import sys
from ngram_builder import build_language_vector

CONFIG_FILE = 'samples.json'

if __name__ == '__main__':
    with open(CONFIG_FILE) as config:
        languages = json.load(config)

    n = int(sys.argv[1])

    for (language, config) in languages.items():
        print language
        vector = build_language_vector(n, config['samples'])
        print vector
