# Conversion Function...

import csv

all_notices = []

with open('todays_notices.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        all_notices.append(row)

print()
print()
for item in all_notices:
    print(item[0])
    print(item[1])
    print()
