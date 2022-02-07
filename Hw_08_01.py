# 8.4  Open the file romeo.txt and read it line by line. For each line, split the line into 
# a list of words using the split() method. The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append 
# it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


flist = list()                      # Assigns empty set to flist
fname=input('Enter file name:')
try:
    fh=open(fname)
except:
    print('File not found')
    quit()

# M E T H O D  1
for line in fh:                     
    word=line.split()           # splits line based on 'space' and assigns the list to the variable 'word'
    for i in word:              # for every word(i.e., 'i') in the list(i.e. 'word')
        if i in flist:          # if word(i.e. 'i') is in the collection, skip to the top.
            continue
        flist.append(i)         # add word(i) to the collection
flist.sort()                    # sort the collection
print(flist)                    # print the collection


#   M E T H O D  2

#for line in fh:                     
#    word=line.split()           # splits line based on 'space' and assigns the list to the variable 'word'
#    for i in word:              # for every word(i.e., 'i') in the list(i.e. 'word')       
#        if not i in flist:      # if word(i.e. 'i') is not in the collection(i.e. flist), append to the list
#            flist.append(i) 
#flist.sort()                    # sort the collection
#print(flist)                    # print the collection


