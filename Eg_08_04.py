# SPLITTING STRINGS INTO LIST
print('EXAMPLE 1')
abc = 'With three words'
stuff = abc.split()     # splits it anytime it meets a space. (i.e. () is the delimiter character
print(stuff,'\n')

print('EXAMPLE 2')
line = 'A lot               of spaces'
etc = line.split()
print(etc,'\n')   # When you do not specify a delimiter, multiple spaces are treated like one delimiter

print('EXAMPLE 3')
line = 'first;second;third'   # There's no space here
thing = line.split()          # the delimiter here was a space. because there is no space in 'line',
print(thing,'\n')                  # it treats the string as one list

print('EXAMPLE 4')
thing = line.split(';')     # we've specified the delimiter as ';'. so where ever the code meets ;,
print(thing,'\n')                # it splits it for the string

print('EXAMPLE 5')
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words,'\n')



# NB;;;;;;;; You can specify what delimiter character to use in the splitting
