# EXAMPLE OF  A CONTINUE STATEMENT

while True:              
    line = input('> ')  # input argument
    if line[0] == '#' : # means that if we input '#' as the 1st character in our argument, it should return to the begining
                        # of the code (i.e., the next line is not triggered). Any thing else triggers the next line
        continue
    if line == 'done' :
        break
    print(line)         # always prints the input input argument, except when the 'done' is triggered.
                        # typing 'done' will break out of the loop. (i.e., line 10 wont trigger)
print('Done!')

# Any argument we input except '#' will skip line 5 and automatically trigger line 8. If the input argument also satisfy
# line 8 condition, the code breaks out of the loop, to line 12.
#  typing #done will not break out of the loop bcos the 1st char is # and will return to the beginning. 