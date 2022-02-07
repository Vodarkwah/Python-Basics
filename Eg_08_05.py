# MORE SLICING EXAMPLES

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    words = line.split()              # split the words according to spaces     
    print(words[2])                   # Prints the 3rd element in every line

