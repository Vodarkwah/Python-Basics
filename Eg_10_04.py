# Real data structures problem
# Sorts the top 10 words in romeo.txt that appears the most

fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items(): # items() breaks dic 'counts' and converts to a list of tuples
    newtup = (val, key)         # creates tuples of val, key pairs for each iteration
    lst.append(newtup)          # appends each tuple into lst and collects them as a list

lst = sorted(lst, reverse=True) # Sorts in descending order of val

for val, key in lst[:10] :
    print(key, val)
