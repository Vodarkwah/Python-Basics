# Wild-Card Characters and fine-tuning
'''
>>> The dot character matches any character
>>> If you add the asterisk character, the character is “any number of times”
'''
count=0
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line) :  # start from X and match all the characters up to : is in the line
        print(line)                # print all line that satisfy the condition
        count=count+1
print(count)