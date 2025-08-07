class Human:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, dob: {self.dob}"

class Employee(Human):
    def __init__(self, name, age, dob, employee_id):
        super().__init__(name, age, dob)
        self.employee_id = employee_id

    def __str__(self):
        return f"{super().__str__()}, employee_id: {self.employee_id}"


e1 = Employee("John", "25", 2021, 123)
print(e1)


