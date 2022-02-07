# 'IS' AND 'IS NOT' LOGICAL OPERATORS

some = [1, 9, 21, 10, 16]
9 in some               # MORE LIKA ASKING A QUESTION THAT 'IS 9 IN SOME'

15 in some

20 not in some          # MORE LIKE SAYING '20 IS NOT IN SOME'

# RESULT WILL SHOW IN THE INTERACTIVE IDE

# FINDING AVERAGES
print('METHOD 1\n')
total = 0
count = 0
while True :
    inp = input('Enter a number: ') #CONVERTS INP TO STR      
    if inp == 'done' : 
        break                #IF 'INP' IS DONE, BREAK OUF OF THE LOOP
    value = float(inp)
    total = total + value     
    count = count + 1

average = total / count
print('Average:', average,'\n')


print('METHOD 2\n')
numlist = list()                #Creates an empty set
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break    # Stops the while loop once done is triggered
    value = float(inp)          # converts str to float
    numlist.append(value)       # appends values into the list

average = sum(numlist) / len(numlist)   # avg
print('Average:', average)
