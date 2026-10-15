import sys
import csv

list1= []
if len(sys.argv) < 3:
    sys.exit('too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('too many command-line arguments')
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(',')
            list1.append({'first' : first.strip(), 'last': last.strip(), 'house': row['house']})
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        (writer.writerow(list1))

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
