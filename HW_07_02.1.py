#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the 
#average of those values and produce an output as shown below. Do not use the sum() function or a variable 
#named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing 
#below enter mbox-short.txt as the file name.

# DESIRED OUTPUT=========Average spam confidence: 0.7507185185185187

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
count = 0
tot=0
#print('cum tot         num')-------Was there to show the summation procedure and the number generated
for line in fh:
    line=line.rstrip()
    if 'X-DSPAM-Confidence:' in line: # if line contains, execute the next line of code
        pos=line.find('0')       # We're finding the position in the line which starts from 0
        num = float(line[pos:])  # We generate the number from the position where 0 is found, up to the end of the line for
                             # each successive line which contains X-DSPAM......
        tot=tot+num              # Summation code
        count=count+1            # we count the no. of lines which contain the X-DSPAM.......
        #print(tot, num)  #Availabe if you wat to see the summation procedure

avg = tot/count     # gives the average of the total sum at the end of the loop and the total count

print('Average spam confidence: ',avg)

#Another way of doing the homework