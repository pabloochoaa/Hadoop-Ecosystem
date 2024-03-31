#!/usr/bin/env python

import sys

accumulator_key = None
accumulator = None

# process the input line by line
for line in sys.stdin:

    # parse the input that has come from the mapper or combiner
    key, value = line.split('\t')

    if key == accumulator_key:
        # still on the same key
        accumulator += int(value)
    else:
        # got a new key
        if accumulator_key:
            # write out the current accumulator
            print('%s\t%s' % (accumulator_key, accumulator))
        # reset for the new key
        accumulator_key = key
        accumulator = int(value)

# write out the current accumulator
if accumulator_key:
  print('%s\t%s' % (accumulator_key, accumulator))
