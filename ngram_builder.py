from classifier import calculate_average_vector
from ngrams import *


def read_sample(file_name):
    with open(file_name) as file:
        return file.read()


def clean_sample(text):
    return deduplicate_whitespace(remove_special_chars(text))


def build_language_vector(n, sample_files):
    samples = [clean_sample(read_sample(sample_file)) for sample_file in sample_files]
    return calculate_average_vector(n, samples)
