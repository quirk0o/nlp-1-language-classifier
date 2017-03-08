# coding=utf-8

from classifier import *
from lcache import LCache
from statistics import *

if __name__ == '__main__':

    sample_sentences = [
        (u'Polish', u'To jest przykladowy tekst. Zostanie wykorzystany do przeanalizowania dzialania klasyfikatora'),
        (u'Polish', u'Szybki brązowy lis skacze nad leniwym psem'),
        (u'English', u'This is a sample sentence. It will be used for language classifier tests.'),
        (u'English', u'The quick brown fox jumps over the laxy dog'),
        (u'Italian', u'Si tratta di una frase di esempio. Sarà usato per i test di lingua classificatore.'),
        (u'German', u'Dies ist ein Beispielsatz. Es wird für den Sprach Klassifikator Tests verwendet werden.'),
        (u'Spanish', u'Esta es una sentencia de la muestra. Será utilizado para las pruebas de lenguaje clasificador.'),
        (u'Spanish', u'El rápido zorro marrón salta sobre el perro perezoso'),
        (u'Finnish', u'Tämä on näyte lause. Sitä käytetään kielen luokitin testejä.'),
        (u'English', u'Sally sells sea shells by the sea shore')
    ]
    classification = map(lambda s: s[0], sample_sentences)

    for n in xrange(1, 12):
        print 'Building language data for n {}'.format(n)
        language_cache = LCache()
        languages = language_cache.build_language_vectors(n)

        classifier = LanguageClassifier(n, languages)
        guesses = []

        for sentence in map(lambda s: s[1], sample_sentences):
            guess = classifier.determine_language(sentence)
            guesses.append(guess)

            print sentence
            print n, guess
            print

        stats = StatisticsService(classification=classification, guesses=guesses)
        print 'Statistics:'
        print 'Precision: {}'.format(stats.average_precision())
        print 'Recall: {}'.format(stats.average_recall())
        print 'F1: {}'.format(stats.f1())
        print 'Accuracy: {}'.format(stats.accuracy())
        print
