class Car:
    wheels = 4  #class variable

    def __init__(self,make,model,year,color):
        self.make = make   #instance variables
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("the "+ self.model+" is driving ")

    def stop(self):
        print("the " + self.model + " has stopped working")
