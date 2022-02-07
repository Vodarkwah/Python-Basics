# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that 
# starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt


fname = input('Enter file name:')

try:
    fh = open(fname)
except:
    print('File not found')
    quit()
count=0
for line in fh:
    if 'From ' in line:             # If 'From' is in the line
        line=line.rstrip()          # stripping off the blank lines as a result of the 'for' statement
        line_split = line.split()   # assigning a new vaible to house the list of lines the contain 'From'
        print(line_split[1])        # prints the 2nd element in the list file for each successive line
        count = count+1             # counting loops 
print('There were',count, 'lines in file with From as the first word')
