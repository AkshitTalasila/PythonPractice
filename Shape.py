class Shape:

    def __init__(self, name = "Unkonw", color = "Unkown"):

        self.name = name
        self.color = color

    def __str__(self):

        return f"Name: {self.name}, Color: {self.color}"

    