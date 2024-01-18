#there are two parts attributes = is/has ex. name,age,height
#methods = actions ex. eat ,sleep etc..
#to create attributes you need to create class(blueprint)

class Car:
 def __init__(self,make,model,year,color):   # in other languages it is called constructor 
    self.make = make 
    self.Model = model
    self.year = year
    self.color = color

 def drive(self):
        print("this "+self.model+" is driving ")
    
 def stop(self):
        print("This "+self.model+" is stopped")

