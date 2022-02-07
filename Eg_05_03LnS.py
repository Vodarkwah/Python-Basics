largest_so_far = None                           # we've represented largest so far with an empty set (i.e. None)
print('Before',largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far is None:                  # more like saying largest so far==None, but 'is' is more powerful than ==
        largest_so_far=num                      # line 4,5 is used for getting started after which it'll be ignored
                                                # once we assign the first value

    elif num>largest_so_far:
        largest_so_far=num
    print(largest_so_far, num)

print('The largest number is',largest_so_far)

smallest_so_far=None
print('Before',smallest_so_far)
for val in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far=val
    elif val<smallest_so_far:
        smallest_so_far=val
    print(smallest_so_far, val)
print('Smallest so far is', smallest_so_far)
