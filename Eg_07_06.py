# USING IN TO SELECT LINES

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line : # were saying that if the line doesnt contain the said str, move to the top
        continue                  # if the line contains the str, print the line that contains the str
    print(line)
