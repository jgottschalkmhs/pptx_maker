# Conversion Function...

import csv

all_notices = []

with open('todays_notices.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        all_notices.append(row)

print()
print()
print(all_notices)
