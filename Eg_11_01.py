# Using re.search() Like find()

print('USING FIND()')
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0: # if there's from in the line
        print(line,)



print('\nUSING RE.SEARCH()')
import re           # imports the regex library

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) : # If there's 'from:' in the line print the line
        print(line)

# both code are the the same