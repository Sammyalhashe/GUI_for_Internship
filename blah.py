"""Uses the RandomWords module offered by Python to generate a random word and serach it on google

Builds the URL
"""
"""Imports

Import Statements for random_words, time, xlsx working
"""
try:
    import os
    from datetime import datetime as dt
    from random import randint
    from random_words import RandomWords
except ImportError as e:
    raise e
    print(e)

"""URL Constants

Constants to build URL search request
"""
REQUEST = "https:"
BASE_SITE = "//www.google.com/search"
SEARCH_QUERY = "?q="

BASE_URL = REQUEST + BASE_SITE + SEARCH_QUERY
toInsertSearch = ""

"""Completing the search query

Generating the random words and adding them to search query
"""
phraseSize = randint(1, 4)
rw = RandomWords()

randomPhrases = rw.random_words(count=phraseSize)

for i in range(len(randomPhrases)):
    BASE_URL += randomPhrases[i] if i == len(randomPhrases) - 1 else randomPhrases[i] + '+'
    toInsertSearch += randomPhrases[i] if i == len(randomPhrases) - 1 else randomPhrases[i] + ' '
os.system('chrome' + ' ' + BASE_URL)
fudged = raw_input('Is it fucked?')

"""Documenting working

Using sheet I made, randomSearchHistory.txt, xlsxutils to write into it
"""
keepGoing = True
START_ROW = 1
COL_SEARCH = 0
COL_DATE = 1

if os.path.isfile('randomSearchHistory.txt'):
    fh = open('randomSearchHistory.txt', 'r+')
    lines = fh.readlines()  # pointer is at end of file
    if not len(toInsertSearch) <= 34:
        fh.write('\n' + toInsertSearch + ' ' * 8 + str(dt.today().strftime('%d, %b %Y')) + ' ' * 8)
    else:
        fh.write('\n' + toInsertSearch + ' ' * (34 - len(toInsertSearch)) + str(dt.today().strftime('%d, %b %Y')) + ' ' * 11 + fudged)
    fh.truncate()
    fh.close()
else:
    fh = open('randomSearchHistory.txt', 'a')
    fh.write('Search                            Date                   Fucked?')
    if not len(toInsertSearch) <= 34:
        fh.write('\n' + toInsertSearch + ' ' * 8 + str(dt.today().strftime('%d, %b %Y')) + ' ' * 8)
    else:
        fh.write('\n' + toInsertSearch + ' ' * (34 - len(toInsertSearch)) + str(dt.today().strftime('%d, %b %Y')) + ' ' * 11 + fudged)
    fh.truncate()
    fh.close()
