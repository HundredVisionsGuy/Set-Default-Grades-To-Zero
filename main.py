# SetDefaultToZero.py
# By HundredVisionsGuy
#!python2
# Takes a Canvas-generated CSV grade export and changes
# all unscored assignments to 0

import csv
import os

# define functions
def addZeroes(file):
    f = open('docs/' + file)
    csv_f = csv.reader(f)
    f_reader = list(csv_f)
    for i in range(len(f_reader)):
        if i < 2:
            continue
        for j in range(len(f_reader[i])):
            #raw_input(f_reader[i][j])
            if j < 3:
                continue
            if f_reader[i][j] == '':
                f_reader[i][j] = '0.0'
        print( f_reader[i])
    return f_reader

def saveFile(filename, inputfile):
    # Build filename
    filename = 'docs/output/' + filename

    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(inputfile)

count = 0
for (dirname, dirs, files) in os.walk('docs'):
   for filename in files:
       if filename.endswith('.csv') :
           count = count + 1
           newFile = addZeroes(filename)

           saveFile(filename, newFile)
