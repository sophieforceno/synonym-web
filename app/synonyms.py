#! /usr/bin/python3

from thesaurus import Word

def get_synonyms(word):
    synonyms = Word(word).synonyms('all')

    if not synonyms:
        synonyms = "No synonyms found"

    return synonyms