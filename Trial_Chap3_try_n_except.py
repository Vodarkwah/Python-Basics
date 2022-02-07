#This is an example in Chapter 3_except_and_try clause
astr='Hello Bob'
try:
    istr=int(astr)
except:
    istr=-1
print('First',istr)

bstr='123'
try:
    instr=int(bstr)
except:
    instr=-1

print('Second', instr)