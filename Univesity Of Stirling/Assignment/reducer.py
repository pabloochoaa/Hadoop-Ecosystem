#!/usr/bin/env python3
import sys
from decimal import Decimal

# Student ID: 3093154

min_votes = 10
print('min_votes = %s' % min_votes, file=sys.stderr)

def reducerLogic(films, years):
# If a film has greater or equal votes as min_votes and has the highest
#   rating for that year (could be shared with other films), it will be 
#   selected
    
    for film in films:
        f_year, f_title = film.split("|")
        votes = films[film][1]
        if votes >= min_votes:
            avgRating = round(films[film][0]/votes, 3)
            if f_year in years.keys():
                if avgRating > years[f_year][0][1]:
                    years[f_year] = [[f_title, avgRating]]
                else:
                    if avgRating == years[f_year][0][1]:
                        years[f_year].append([f_title, avgRating])
            else:
                years[f_year] = [[f_title, avgRating]]

# Create the variables that will store the info (title, year, rating 
#    and number of occurences) of a film over the iterations.
current_film = None
current_year = None
rating_acc = 0
number_acc = 0

# Dictionary that will store a list of all the highest rated films of a year
years = {}
# Dictionary that will store partial results for each film
films = {}

# Process the input line by line
for line in sys.stdin:

    # Parse the input line
    year, title, rating, number = line.split('\t')

    # Parse the numeric values to their corresponding type
    #   (as they are passed as strings)
    value_number = int(number)
    value_rating = Decimal(rating)
    
    # If the film is the same as the previous one, we only update the num of occurences
    #   and add the ratings (as we can't calculate the total average now)
    if title == current_film:
        number_acc = number_acc + value_number
        rating_acc = rating_acc + value_rating 
    else:
        # If the film is different from the previous one, and the previous one has
        #   more or equal votes as "min_votes", the logic method is called
        if current_film:
            # This will be the key as it is more efficient than having to 
            #   look for the year in the dictionary (as year cannot be the key)
            auxKey = current_year+"|"+current_film 
            if auxKey in films.keys():
                films[auxKey][0] = rating_acc + films[auxKey][0]
                films[auxKey][1] = number_acc + films[auxKey][1]
            else:
                films[auxKey] = [rating_acc, number_acc]      
            	
        # Update the vars to the current film        
        current_film = title
        current_year = year
        rating_acc = value_rating
        number_acc = value_number

# Save last film, as in the loop it would not be saved
#    (no new films are coming)
if current_film:
    auxKey = current_year+"|"+current_film 
    if auxKey in films.keys():
        films[auxKey][0] = rating_acc + films[auxKey][0]
        films[auxKey][1] = number_acc + films[auxKey][1]
    else:
        films[auxKey] = [rating_acc, number_acc]  

reducerLogic(films, years)

# Print all the highest rated films per year
for film_year in years:
    for film in years[film_year]:
        print(f"{film_year}\t{film[0]}\t{film[1]}")