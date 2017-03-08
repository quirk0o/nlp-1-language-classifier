import string
import sys

from classifier import *


def read_sample(file_name):
    with open(file_name) as file:
        return file.read()


def clean_sample(text):
    return deduplicate_whitespace(remove_special_chars(text))


if __name__ == '__main__':
    alphabet = string.ascii_lowercase + ' '
    n = int(sys.argv[1])

    samples = [clean_sample(read_sample(sample_file)) for sample_file in sys.argv[2:]]
    vector = calculate_average_vector(n, samples)
    print vector
