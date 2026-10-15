import sys
from tabulate import tabulate
import csv


csv_list = []

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith('.csv') == False:
    sys.exit('Not a CSV file')
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers = 'keys', tablefmt='grid'))


except FileNotFoundError:
    sys.exit('File does not exist')











