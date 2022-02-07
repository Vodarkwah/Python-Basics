# Adding New Entries to the Dictionary 

# METHOD 1-------USING CONDITIONAL STATEMENT
print('\nMethod 1\n')
counts = dict()     # creates an empty dict file i.e. {}
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :         # for every list in the variable 'names'
    if name not in counts:  # if the list is not in the dict variable 'counts'
       counts[name] = 1     # create an new entry(key) and a value of 1
    else :
        counts[name] = counts[name] + 1     # if list in counts, add a value of 1 to the existing value
print(counts,'\n')               # print everything when done.


# METHOD 2------USING THE GET() METHOD
print('Method 2')

if name in counts:
    x = counts[name]
else :
    x = 0

# x = counts.get(name, 0) # we need to input a name. if the name is present in dic, it'll print the value of
# the name(key) else, it return 0 as default if the key is not in dic

x=counts.get('zqian',0) # entering the name/key (i.e zquian) gives the value of the name, i.e.1
print(x)

# NB. The get() statement is for checking to see if a key is already in a dictionary and 
# assuming a default value if the key is not there.
# Returns the valueof key if key is in dic and returns default value if key does not exist
# Get() does not return tracebacks