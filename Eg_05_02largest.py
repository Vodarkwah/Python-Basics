largest_so_far = -1
print('Before',largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far, the_num)

print('The largest number is',largest_so_far)

smallest_so_far=100000
print('Before',smallest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num<smallest_so_far:
        smallest_so_far=num
        print(smallest_so_far)
print('Smallest so far is', smallest_so_far)

# This code is too basic. The correct code is done in Eg_05_03