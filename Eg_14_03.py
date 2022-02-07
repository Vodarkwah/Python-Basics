# Application of Instance Variables

class PartyAnimal:
   x = 0                # class variable------This is shared by all obj instances in a class
   name = ""            # instance variable, you can ignore this line of code
                        # self is the attribute of the class and has to be present
   def __init__(self, z): # z ---- parameter associated with the instance variable 'name'
     self.name = z         # code used to assign variables to the attribute
     print(self.name,"constructed") # Prints the name(i.e. the variable) + constructed

# Does not repeat already entered entries. Eg. repeat of s.party() will not result in 
# Sally constructed being repeated

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()


'''  NB. Constructors can have additional parameters that can be used to set up instance variables

in Ln 5, name = "" is an instance variable. 
self is the attribute and always comes first. You cannot do away with the self, else it'll result
in syntax error

'''