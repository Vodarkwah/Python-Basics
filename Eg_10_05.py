# SHORTER METHODS OF SORTING VALUES INSTEAD OF KEY

c = {'a':10, 'b':1, 'c':22}

#print( sorted( [ (v,k) for k,v in c.items() ] ) ) -------prints list of tuples sorted by val

cf=sorted( [ (v,k) for k,v in c.items() ] )     # Stores list of tuples as cf by val

for v,k in cf:
    print(v,k)              # prints val , key 