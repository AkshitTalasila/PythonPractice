class Employee:

    def __init__(self,name = "Jhon Doe", employee_id = 0000, salary = 0000):

        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):

        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"

    