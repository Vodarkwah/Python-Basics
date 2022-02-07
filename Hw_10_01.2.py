# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour 
# of the day for each of the messages. You can pull the hour out from the 'From ' line by finding 
# the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname= input('Enter file name:')
counts={}
lst_hr=[]
try:
    fh=open(fname)
except:
    print('File not found')
    quit()

for line in fh:
    if 'From ' in line:             # Searches for 'From ' for each line through file
        line=line.split()           # splits each line into list based on spaces
        words=line[5]               # stores the 6th element of each line into words
        time=words.split(':')       # spiits words by ';' and stores as time(collection)
        time_hr=time[0]             # stores the first element of each time as time_hr
        counts[time_hr]=counts.get(time_hr,0)+1     # Creates new entries into counts using hr variable
#print(count)

print(sorted([(k,v) for k,v in counts.items()]))