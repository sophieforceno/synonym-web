#! /usr/bin/python3

from PyDictionary import PyDictionary

dictionary = PyDictionary()


def get_defin(word):
    defin = dictionary.meaning(word)
    # Crude, but effective for now
    if not defin:
        defin = "No definitions found"

    return defin
