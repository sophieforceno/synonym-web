#! /usr/bin/python3

from PyDictionary import PyDictionary

dictionary = PyDictionary()

def get_defin(word):
    defin = dictionary.meaning(word)

    if not defin:
        defin = "No definitions found"

    return defin