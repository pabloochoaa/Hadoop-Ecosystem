#!/usr/bin/env python

import sys
import string

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# input comes from STDIN (standard input)
eprint("Hello")
for line in sys.stdin:
    sizes = {}
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # We print out a word, a tab character and a count of 1

        for punct in string.punctuation:
            word = word.replace(punct, "")
        word = word.lower()

        length = len(word)
        if length in sizes:
            sizes[length] += 1
        else:
            sizes[length] = 1

    for key in sizes.keys():
        print('%s\t%s' % (key, sizes[key]))
