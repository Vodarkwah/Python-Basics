# COUNTING LINES IN A FILE

count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    count=count+1
print('Line Count: ',count)