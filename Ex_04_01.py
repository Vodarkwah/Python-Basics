#Write a program to prompt the user for hours and rate per hour 
#using input to compute gross pay. Pay should be the normal rate for hours up to 40 
#and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() 
#and use the function to do the computation. The function should return a value. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay shlould be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume 
#the user types numbers properly. Do not name your variable sum or use the sum() function.
r=float(input('enter rate: '))
h=float(input('enter hours: '))
def compute_pay(r,h):
    if h>40:
        pay = (1.5*r*(h-40))+(40*r)
        return pay
    else:
        pay=h*r
        return pay

pay=compute_pay(r,h)        #Need to assign a variable to the function to store the value
print('Pay',pay)

#def added(a,b):            This was just a trial
 #   x=a+b
  #  return(x)

#x=added(3,2)
#print(x)