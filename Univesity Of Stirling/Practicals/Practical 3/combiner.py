#!/usr/bin/env python

# NB: Hadoop might not run this

import sys

# create aux variables

current_word = None
current_count = 0
word = None

# process the input line by line
for line in sys.stdin:
    line = line.strip()

    # get the word and count from the line
    word, count = line.split('\t', 1)

    # The count is passed as a string, so in the addition
    #     the result would be wrong otherwise
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # print(f"word = {word} and count = {count}", file=sys.stderr)
    
    # if the word has changed, print count 
    #    and get the next one as current
    if word != current_word:
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
        # print(f"new_word = {word} and its count = {count}", file=sys.stderr)
    else:
        # if the word is the same, we add the count up
        current_count = current_count + count
        # print(f"add of count is {current_count}", file=sys.stderr)

# print the last word, as otherwise in the past loop wouldn't 
#     be printed (no new words are coming)
print(f"{current_word}\t{current_count}")
