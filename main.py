# SetDefaultToZero.py
# By HundredVisionsGuy
# Takes a Canvas-generated CSV grade export and changes
# all unscored assignments to 0

import csv
import os

#
count = 0
for (dirname, dirs, files) in os.walk('docs'):
   for filename in files:
       if filename.endswith('.csv') :
           count = count + 1
print 'Files:', count

# Loop through rows
