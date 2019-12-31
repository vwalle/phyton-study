"""
Start by reading a pre-filled array; in future versions we will feed the array
The name of the file will be pre-filled array
"""
"""
import csv

with open('Pre-filled Array', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
print(spamreader)
"""

#f = open('Pre-filled Array', 'r')
#x = f.readlines()
with open('Pre-filled Array', 'r') as f:
    x = f.read().splitlines()
f.close()
r1= [int(n) for n in x[1].split(",")] #  x[1].split()
print(r1)
