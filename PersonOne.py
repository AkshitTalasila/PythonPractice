class PersonOne:

    def __init__(self,name = "Unkown", phone = "000-000-000"):

        self.name = name
        self.phone = phone

    def __str__(self):

        return f"Name: {self.name}, Phone: {self.phone}"

    