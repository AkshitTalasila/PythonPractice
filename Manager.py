from Employee import Employee

class Manager(Employee):

    def __init__(self, name = "Jhon Doe", employee_id = 0000, salary = 0000, department = "None", num_employee =0):

        super().__init__(name,employee_id,salary)
        self.department = department
        self.num_employee = num_employee

    def __str__(self):

        return f"{super().__str__()}, Department: {self.department}, Employess Working Under: {self.num_employee}"

    def giveRaise(self,amount:float):

        self.salary +=amount


m1 = Manager("John", 1234, 75000, "Engineering", 10)
print(m1)
m1.giveRaise(1000)
print(m1)