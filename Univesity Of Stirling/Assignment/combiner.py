#!/usr/bin/env python3
import sys
from decimal import Decimal

# Student ID: 3093154

# Create the variables that will store the info (title, year, rating 
#    and number of occurences) of a film over the iterations.
number_acc = 0
rating_acc = 0
current_film = None
current_year = None

# Process the input line by line
for line in sys.stdin:
    # Read the line and store the info in the corresponding vars
    year, title, rating, number = line.strip().split("\t")

    # Parse the numeric values to their corresponding type
    #   (as they are passed as strings)
    value_rating = Decimal(rating)
    value_number = int(number)

    # If the film is the same as the previous one, we only update the num of occurences
    #   and add the ratings (as we can't calculate now the total average)
    if title == current_film:
        number_acc += value_number
        rating_acc += value_rating 
    else:
        # If the film is the different from the previous one (and the var is not None),
        #   we print the information of the film to pass it to the reducer
        if current_film:
            print(f"{current_year}\t{current_film}\t{rating_acc}\t{number_acc}")	        
        # Once printed the previous film, update the vars to the current film
        current_film = title
        current_year = year
        number_acc = value_number
        rating_acc = value_rating

# Print last film, as in the loop it would not be printed
#    (no new films are coming)
if current_film:
    print(f"{current_year}\t{current_film}\t{rating_acc}\t{number_acc}")