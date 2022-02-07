# EXAMPLE OF A BREAK STATEMENT

while True:
    line=input('> ')
    if line == 'done' :
        break   #Once we type done, the while loop breaks. While the condition
                #is not satisfied, the "Done" syntax cannot be run
                #The code will not stop until the condition for the if statement
                #is satisfied
    print(line) #Loop ends here and returns to the input argument until the right variable is trigered
                #it prints every argument typed 

print('Done!')
