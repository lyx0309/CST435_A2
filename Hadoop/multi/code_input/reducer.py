#!/usr/bin/env python
"""reducer.py"""

import sys

current_country = None
current_sum = 0
counter = 0
averages = []

# loop through lines in input
for line in sys.stdin:
    # remove unnecessary whitespace
    line = line.strip()

    # extract country and views from the line
    try:
        country, views = line.split('\t', 1)
        views = int(views)
    except ValueError:
        # ignore lines with invalid data like excel header row
        continue

    # since lines with same key should be adjacent to one another, can use this this method to accumulate the sum views>    if current_country == country:
        current_sum += views
        counter += 1
    else:
        # if this is a new country, calculate the average views of previous country directly, stored it to a list
        if current_country is not None and counter != 0:
            average = round(float(current_sum) / counter, 2)
            averages.append((current_country, average))

        # reset variables for the new country
        current_country = country
        current_sum = views
        counter = 1

# calculate average for the last country
if current_country == country and counter != 0:
    average = round(float(current_sum) / counter, 2)
    averages.append((current_country, average))

# sort averages and get the top 5
top_5 = sorted(averages, key=lambda x: x[1], reverse=True)[:5]

# print the top 5 countries based on their averages
for country, average in top_5:
    print '%s\t%s' % (country, average)