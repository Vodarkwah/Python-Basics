# REVIEWING CONCEPTS THAT MAY HAVE BEEN LEFT OUT
# CH.4.4 ----MATH FUNCTIONS (BOOK-Pythonlearn_2)

# Python has a math module that provides most of the familiar math functions.
# Before we can use the module, we have to import it


import math

print(math.log10(10))       # more like saying log 10(10), available for base 2 and 10

print(math.sin(180))        # sin is in rad 

# trigonometric functions (cos, tan, etc.) take arguments in radians. 
# To convert from degrees to radians, divide by 360 and multiply by 2*pi


d= 45       # angle in degrees
r=d/180*math.pi     # conversion from deg to rad

print(math.sin(r))   # sin of 45deg


print(math.sqrt(4))

# check dir(math) to know what works with math fns