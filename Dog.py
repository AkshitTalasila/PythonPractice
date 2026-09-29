from Animal import Animal

class Dog(Animal):

    def __init__(self,name = "DogName", age = 0,breed="DogBreed"):

        super().__init__(name,age)
        self.breed = breed

    def __str__(self):

        return f"{super().__str__()} ,Breed: {self.breed}"


d1 = Dog("Buddy", 5, "Golden Retriver")
print(d1)

