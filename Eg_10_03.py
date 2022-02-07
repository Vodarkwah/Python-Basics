# SORTING TUPLES USING VALUES INSTEAD OF KEYS

c = {'a':10, 'b':1, 'c':22}
tmp = list()                    # Creates a new list
for k, v in c.items() :         
    tmp.append( (v, k) )        # adds value, key pairs to the list which in turn creates a list of tuples
print(tmp)
tmp = sorted(tmp, reverse=True) # Reverse=True sorts from high to low
print(tmp)


# we construct a list of tuples of the form (value, key) which we could sort by value
# We do this with a for loop that creates a list of tuples  
