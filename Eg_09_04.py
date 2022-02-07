# SPLITTING AND COUNTING WORDS IN A DOC/TXT

# BASIC CODE
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()        # Splits line according to space
print('Words:', words)      # prints a list of words
print('Counting...')        
for word in words:          # for every word in list(words)
    counts[word] = counts.get(word,0) + 1   # update both existing and new words in dict()
print('Counts', counts)     # print the resulting dict

# NB-----The general pattern to count the words in a line of text is to split the line into words, then loop 
# through the words and use a dictionary to track the count of each word independently. (Too Basic)

#for a in counts:
#    print(a,counts[a])         #this prints the key and its corresponding value