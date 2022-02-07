# DELETING ELEMENT FROM LIST

# If you know the index of the element you want, you can use pop():
print('STAGE 1')
t = ['a', 'b', 'c']
x = t.pop(1)            # removes the second element
print(t)        
print(x,'\n')


# If you don’t need the removed value, you can use the del operator:
print('STAGE 2')
t = ['a', 'b', 'c']
del t[1]
print(t,'\n')


# If you know the element you want to remove (but not the index), you can use remove:
print('STAGE 3')
t = ['a', 'b', 'c']
t.remove('b')
print(t)

print('ALTERNATIVELY, STAGE 4',t.remove('a')) #The return value from remove is None 


# To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print('Using del',t)



