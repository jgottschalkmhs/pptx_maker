# Conversion Function...

import csv


# *** Generate food dictionary *****
# open file
notices = open('todays_notices.csv')

# Read data into a list
csv_notices = csv.reader(notices)

for row in notices:
    print(row)

