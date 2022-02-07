# Object life cycle

class PartyAnimal:
   x = 0

   def __init__(self):              #__init__()------constructor
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):               # destructor
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)




# In object oriented programming, a constructor in a class is a special block of statements called 
# when an object is created
