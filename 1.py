import json
import sys

from classifier import *


def read_sample(file_name):
    with open(file_name) as file:
        return file.read()


def clean_sample(text):
    return deduplicate_whitespace(remove_special_chars(text))


CONFIG_FILE = 'samples.json'

if __name__ == '__main__':
    with open(CONFIG_FILE) as config:
        languages = json.load(config)

    n = int(sys.argv[1])

    for (language, config) in languages.items():
        print language
        samples = [clean_sample(read_sample(sample_file)) for sample_file in config['samples']]
        vector = calculate_average_vector(n, samples)
        print vector
