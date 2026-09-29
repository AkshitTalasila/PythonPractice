from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self,make = "Unkonwn", model = "Unkown", year = 0000, num_doors = 0, isElectric = False):

        super().__init__(make,model,year)
        self.num_doors = num_doors
        self.isElectric = isElectric

    def __str__(self):

        return f"Make: {self.make}, Model: {self.model}, Year Made: {self.year}, Number of Doors: {self.num_doors}, Electric: {self.isElectric}"


car1 = Car("Tesla", "Model 3", 2025, 4, True)
car2 = Car("Honda", "Civic", 2022, 4, False)

print(car1)
print(car2)