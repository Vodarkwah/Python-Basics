#Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'. Once 'done' is entered, print out
#the largest and smallest of the numbers. If the user enters anything
#other than a valid number catch it with a try/except and put out an
#appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4
#and match the output below.

#invalid input
#Maximum is 10
#Minimum is 2

largest = None      #Assigns an empty set to both variables
smallest = None
while True:         #Statement is always true
    num = input('Enter any integer number: ')   #Prompts user for integer num
    try:    
        num = int(num) #input is always in string hence we use this to force-convert the varaible to integer
        
        if largest is None:
            largest=num
        elif num>largest:
            largest=num
        if smallest is None:
            smallest = num
        elif num<smallest:
            smallest=num 
    except:     #If we cant force-convert/if the try clause fails
        if num == 'done':
            break   #Once we type done, the code breaks out of the loop to the next set of code
        else: 
            print('Invalid Input')  #This is where the indefinite loop ends

print('Maximum is', largest)
print('Minimum is', smallest)