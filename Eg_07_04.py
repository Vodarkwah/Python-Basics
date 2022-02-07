# SEARCHING THROUGH A FILE

fhand = open('mbox-short.txt')      # File handler to store mbox as a sequence of strings
for line in fhand:                  # code initiator
    if line.startswith('From:') :   # condtition
        print(line)                 # whereever we see 'From:' as a sentence starter, print the whole sentence 

# This code leaves a blank line in successive statements
# The code below is used to remove the blanklines from the code

fh=open('mbox-short.txt')           #There are two ways to strip off the spacce as shown below
for l in fh:                        #code 1 
    l=l.rstrip()                    # Code 2-----The code in line 13can be moved to line 15
    if l.startswith('From:'):
        print(l)