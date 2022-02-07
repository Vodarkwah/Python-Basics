# More finetuning examples

count=0
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S+:', line) :  # start from X and match all non-whitespace up to : is in the line
#                                   # means that any line that has a space in it prior to reaching : is ignored
        print(line)                # print all line that satisfy the condition
        count=count+1
print(count)

