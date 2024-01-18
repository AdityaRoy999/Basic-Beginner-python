#there are two parts attributes = is/has ex. name,age,height
#methods = actions ex. eat ,sleep etc..
#to create attributes you need to create class(blueprint)

class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("the "+ self.model+" is driving ")

    def stop(self):
        print("the " + self.model + " has stopped working")
