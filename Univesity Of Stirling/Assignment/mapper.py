#!/usr/bin/env python3
import sys

# Student ID: 3093154

# Read included years
with open('years.txt', 'r') as f:
    included_years = f.read().split()

years_empty = len(included_years) == 0

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    uid, title, genres, year, rating = line.strip().split('\t')

    # We check if the years file is not empty as if it is empty
    #   there will be no restriction of years in the calculations  
    if not years_empty:
        # Check if the year of the film is in said file to eliminate
        #   unwanted data from the start to be more efficient
        if year in included_years:
            genres_list = genres.split("|")
            for genre in genres_list:
                print(f"{year}\t{title}\t{rating}\t{1}") 
    else: 
        genres_list = genres.split("|")
        for genre in genres_list:
            print(f"{year}\t{title}\t{rating}\t{1}")  
    