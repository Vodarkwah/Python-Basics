# SKIPPING WITH CONTINUE

fhand = open('mbox-short.txt')
for line in fhand:                  # More lke the code in Eg_07_04 but we're saying that when
    line = line.rstrip()
    if not line.startswith('From:') : # the statement doesnt start with From:,skip and move to the beginining of the 
        continue                   # code. If code starts with From:, it executes line 8  
    print(line)

# Means that while true, dont break put of the loop(i.e., move to the top). if code starts with from, 
# it becomes false and hence line 8 is triggered