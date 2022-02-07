# EXAMPLES OF REGEC=X VERSION

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)  # look for lines that start wuth X-....:
#   #start extrac from numeric char from [0-9. (. rep the dec pt).] + to repeat for rest of line

    if len(stuff) != 1 :  continue  # If not found, skip the line
    num = float(stuff[0]) # convert str in list to num
    numlist.append(num)   # adds the num to the list 'numlist'

print('Maximum:', max(numlist)) # prints the max no in the list (NB: max fn)