class Animal:

    def __init__(self, name = "generic", age = 0):

        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


