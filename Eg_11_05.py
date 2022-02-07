# REGEX VERSION OF DOUBLE SPLIT STRING EXTRACTION

import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)  # Look through the str until you find @ sign. Start str extrac and find all
#                               # non-space char 
print(y) 

# A MORE PRECISE VERSION
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)  # look for str startong with 'From ' looking for @ sign. Start str extrac 
#                                       # and find all non-space char 
print(y)
