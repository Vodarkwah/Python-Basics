#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.
#Enter Hours: 20 
#Enter Rate: nine 
#Error, please enter numeric input
#Enter Hours: forty  
#Error, please enter numeric input



try:
    hr = float(input('Enter the number of hours: '))
    rate = float(input ('Enter the rate per hour spent: '))

except:
    print('Enter a Numeric value for rate and hours spent')
    quit()

if hr > 40:
    pay = (1.5*rate*(hr-40))+(40*rate)
    
else:
    pay=hr*rate
    

print('Pay: ',pay)
