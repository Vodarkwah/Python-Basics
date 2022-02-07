# LIST METHODS

# LIST.append(ELEMENTT) adds a new element to the end of a list:
t = ['a', 'b', 'c']
t.append('d')
print(t)

# L1.extend(L2) takes a list as an argument and appends all of the elements:
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)           # NB-----This example leaves t2 unmodified.

