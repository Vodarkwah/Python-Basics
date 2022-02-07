# COUNTING THE NUMBER OF STRINGS
fruit = 'banana'
count=0

while count < len(fruit):   # line 5,6 is used to count the total number of characters in the variable
    count=count+1
print(count)


index = 0                   # this code is used to specifically count the number of times a particular
for i in fruit:             # letter appears in a text
    if i=='a':
        index = index+1
print(index)

