# PROMPTING USER FOR FILES

fname = input('Enter the file name:  ')
try:
      fhand = open(fname)
except:
      print('File cannot be opened:', fname)
      quit()            # withou quit(), the execution will proceed, which inturn will bring tracebacks
                        # one quit() is there, an error will jus terminate the whole code and prevent 
                        # codes from line 12 to run

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

