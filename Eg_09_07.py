# finding the most appearing word in a file

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:             # for every line in file handle
    words = line.split()        # split line according to spaces and stores them in variable 'words'
    for word in words:          # for every word in words,
        counts[word] = counts.get(word,0) + 1   # create a new entry in dic counts. adds 1 if entry already exists

# At this pt, it is done compiling the dict counts

bigcount = None             # empty set for bigcount
bigword = None              # empty set for bigword
for word,count in counts.items():  # for k,v in items(k,v in dic counts)
    if bigcount is None or count > bigcount: # if bc(i.e val of variable'key') is empty or 
                                            #count(i.e.value of the key) > bc
                                            
        bigword = word                       # if condition is satisfied, stores the word
        bigcount = count                     # if condition is satisfied, stores the count
# we compare values in this case to campare the maximum value and later correspond it to the word.
print(bigword, bigcount)
