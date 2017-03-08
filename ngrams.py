import re


def remove_special_chars(text):
    return re.sub('[^a-z\s\n\r\t]+', '', text)


def deduplicate_whitespace(text):
    return re.sub('[\s\n\r\t]+', ' ', text)


def generate_ngrams(n, text):
    return [text[i:i+n] for i in xrange(len(text) - n+1)]
