# Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, 
#print a suitable error message and exit. For the test, enter a score of 0.85.

s=input('Please enter your score: ')
try: 
    s=float(s)
    if 0.0>s>1.0:
        print('Sorry, The score should be between 0.0 and 1.0')
        
except:
    print('Sorry, enter a numeric value')
    quit()   

if 0.9<=s<=1.0:
    print('A')
elif 0.8<=s<0.9:
    print('B')
elif 0.7<=s<0.8:
    print('C')
elif 0.6<=s<0.7:
    print('D')
elif 0<=s<0.6:
    print('F')
else:
    print('Enter a numeric value between 0 and 1 to check grade')
    quit()
print('All done!')
