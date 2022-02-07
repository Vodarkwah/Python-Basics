# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
# number of mail messages. The program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's 
# mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most prolific committer.
# Desired output ------------------ cwen@iupui.edu 5

mostmail= None              # the key for the most mail
countmail= None             # value associated with the key
counts=dict()               # new dict called counts
fname= input('Enter file name:\n')
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

for line in fh:            
    line=line.rstrip()
    if 'From ' in line: # The space in front of the From is very important
                        # Brings out all lines the contain 'From ' in line
        words=line.split() # Splits line according to space and stores list as words for each line
        mail= words[1]     # Creates a variable 'mail' that stores 2nd element for each line

        counts[mail]=counts.get(mail,0)+1   # Stores the corresponding mail and the number of times they appear
        #if mostmail is None or countmail>

for key,val in counts.items():  # For key and value in the dictionary
    if countmail is None or val > countmail:    # Consult Eg_09_07.py for more details
        mostmail=key    # Stores new greater val's word for every new large count
        countmail=val   # Stores every new large number/value in the dict
print(mostmail,countmail)



# print(mail)
#print(counts)




            