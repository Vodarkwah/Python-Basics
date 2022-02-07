# GREEDY AND NON- GREEDY MATCHING

print('GREEDY MATCHING')
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)  # '+ 'is for greedy matching and hence all words that satisfy the condition is read
print(y,'\n')    # prints out the largest str


print('NON-GREEDY MATCHING')
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) # Once it satisfies the cond, it chills and dont move outward
print(y)    # Prints out the first occurrence
