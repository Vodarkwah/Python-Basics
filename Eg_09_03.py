# SIMPLIFIED COUNTING WITH GET()

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :                             # for every variable in the list
    counts[name] = counts.get(name, 0) + 1      # if key is not in dict, assign key(i.e return default val +1), else
                                                # old key val + 1
print(counts)


# We can use get() and provide a default value of zero when the key is not yet 
# in the dictionary - and then just add one
# NB-----line 6 combines both if and else statement