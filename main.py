# SetDefaultToZero.py
# By HundredVisionsGuy
# Takes a Canvas-generated CSV grade export and changes
# all unscored assignments to 0

import csv
import os

# define functions
def addZeroes(file):
    f = open('docs/' + file)
    csv_f = csv.reader(f)
    for row in csv_f:
        print row

count = 0
for (dirname, dirs, files) in os.walk('docs'):
   for filename in files:
       if filename.endswith('.csv') :
           count = count + 1
       addZeroes(filename)
       print '\n\nDone\n\n'
print 'Files:', count



# Loop through rows
