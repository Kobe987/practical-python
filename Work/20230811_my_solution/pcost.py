# pcost.py
#
# Exercise 1.27
import csv
f = open('Data/portfolio.csv', 'rt')
rows = csv.reader(f)
headers = next(rows)
total = 0

for row in rows:
    total += float(row[2])*float(row[1])

print("Total cost", total)
f.close()
