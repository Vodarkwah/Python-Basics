# SORTING IN TUPLES

# METHOD 1

d = {'a':10, 'b':1, 'c':22}
print(sorted(d.items()),'\n')


# METHOD 2
for k, v in sorted(d.items()):    # Sorts in order of key
    print(k, v)     
