# Definite Loops and Dictionaries
counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:          # creates a variable 'key' that loops through the dic to obtain the keys
    print(key, counts[key]) # prints the keys and thier corresponding variables in the dic


# Retrieving List from dic

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))            # prints list form dic (i.e. the keys)
print(jjj.keys())           # same code as line 10. also prints keys from dic
print(jjj.values())         # prints val of the keys in  the dic
print(jjj.items())          # Introduces a new concept called Tupples


