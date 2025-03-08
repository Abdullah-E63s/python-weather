class Car:
    # special method
    def __init__(self, make, model, year, color):
     self.make = make     # attributes
     self.model = model
     self.year = year
     self.color = color



    def drive (self):
        print("this " +self.model+ " is driving")   # methods 

    def stop(self):
        print("this " +self.model+ " is stopped")