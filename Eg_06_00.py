# FORMATTING IN STRING

# We use %d to format an integer, %g to format a floating-point number, and %s to format a string

camels = 42
print('%d' % camels)  # 42 here is an int not a str

print('I have spotted %d camels.' % camels)

print('In %d years I have spotted %g %s.' %( 3, 0.1,'camels'))

# NB------If there is more than one format sequence in the string, the second argument has to be a tuple. 
# Each format sequence is matched with an element of the tuple, in order.  As in line 10