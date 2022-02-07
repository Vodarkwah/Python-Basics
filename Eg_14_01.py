# Introduction to object orientd programming

class PartyAnimal:          # Defines a class --- PartyANimal
    x = 0                   # Each PartyAnimal object has a bit of data. it is the object operator
                            # The fn looks up to it

    def party(self) :
      self.x = self.x + 1
      print("So far",self.x)

an = PartyAnimal()  #Construct a PartyAnimal object and store in 'an'

an.party()
an.party()
an.party()

# type ----- to identify the kind of obj whether str, list, dic, class, etc
# dir  ----- to identify the capability of  the obj

print(type(an),'\n', dir(an))
