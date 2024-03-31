#!/usr/bin/env python

import sys
import re

# process the input line by line
for line in sys.stdin:

    # make the line lowercase, remove punctuation, split into words
    words = re.sub(r'[^a-zA-Z0-9\'\s]', '', line.strip().lower()).split()

    for word in words:

        # emit
        print('%s\t%s' % (word, 1))
        
