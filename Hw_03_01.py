#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate 
#for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number.

#Desired output------------498.75
#code should contain an if statement

#hrs=47.5 #rate=10

h=float(input('Enter the hours spent:'))
r=float(input('Enter the rate per hours spent:'))
if h>40:
    pay=(1.5*r*(h-40))+(40*r)

else:
    pay=h*r
print(pay)

