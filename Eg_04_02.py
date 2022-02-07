# 4.5 Random numbers

# The random module provides functions that generate pseudorandom numbers

import random       # Imports the random module

n=[]
i=0
while i<20:
    a= random.randint(0,37) # generates random int from 0-37
    i=i+1
    n.append(a) # creates a list n and collects the int into it
print(n)


# The function random returns a random float between 0.0 and 1.0 (including 0.0
# but not 1.0)

for i in range(10):  
    x = random.random()
    print(x)
# This program produces the following list of 10 random numbers between 0.0 and
# up to but not including 1.0.


t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))

# To choose an element from a sequence at random, you can use choice
