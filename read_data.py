
from io import StringIO
import csv

data_2d = []
with open('pairwise_credit_small.csv', newline='\n') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader) # this will skip that header
    for row in reader:
      data_2d.append([x for x in row])

for i in range (len(data_2d)) :
    print(data_2d[i],'\n')

print(len(data_2d))


