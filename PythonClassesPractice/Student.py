from PythonClassesPractice.Person import Person

class Student(Person):

    def __init__(self, major="N/A", grad_year="00", phone="444",adress="123 fake street", name="none"):

        super().__init__(phone, adress, name)

        self.major = major
        self.year = "Freshman"
        self.ID = "1"
        self.grad_Year = grad_year

    # basically a to string
    def __str__(self):
        return self.get_name()


s1 = Student()

s1.set_name("hi")
print(s1)
print(s1.get_name())