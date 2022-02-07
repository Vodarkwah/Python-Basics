# DOUBLE SPLIT PATTERN

line='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()        # Splits according to space
email = words[1]            # stores the 2nd element as email
pieces = email.split('@')   # splits email according to '@' as the delimiter
print(pieces[1])            # prints the 2nd element of the email variable

