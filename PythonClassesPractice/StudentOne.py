from PersonOne import PersonOne

class StudentOne(PersonOne):

    def __init__(self, name = "Unkonwn", phone ="000-000-000" , major = "Undeclared", grad_year = "2030"):

        super().__init__(name,phone)
        self.major = major
        self.grad_year = grad_year


    def __str__(self):

        return f"{super().__str__()}, Major: {self.major}, Graduation Year: {self.grad_year}"
    
s1 = StudentOne("Alex", "555-1234", "Computer Science", 2028)
s2 = StudentOne()

print(s1)
print(s2)
