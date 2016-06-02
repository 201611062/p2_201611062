class Dog(object):
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def dog(self):
        print "My dog name is ",self.name+" and species is ",self.species+" and sounds mung mung"
        
        
class Shihtzu(object):
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def dog(self):
        print "My dog name is ",self.name+" and species is ",self.species+" and sounds si si"
        
class Maltese(object):
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def dog(self):
         print "My dog name is ",self.name+" and species is ",self.species+" and sounds mal mal"

dogname=raw_input("Write dog name : ")
dogsound=raw_input("Write dog species : ")
if dogsound=="Shihtzu":
    answer=Shihtzu(dogname,dogsound)
    answer.dog()
elif dogsound=="Maltese":
    answer=Maltese(dogname,dogsound)
    answer.dog()
else:
    answer=Dog(dogname,dogsound)
    answer.dog()

raw_input("")