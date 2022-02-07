# looping through STRINGS
print('METHOD 1')
fruit='banana'
count=0
print(fruit)

while True:
    letter = fruit[count]
    print(letter, count)
    count=count+1
    if count ==len(fruit):
        break

print('\n\n')
print('METHOD 2')
#Another way of writng the code
index=0
fruit='banana'
while index<len(fruit):
    place= fruit[index]
    print(index,place)
    index=index+1


print('METHOD 3')
for pos in fruit:
    print(pos)