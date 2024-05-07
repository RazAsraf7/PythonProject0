class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def details(self):
        super().details()
        print(self.salary)

emp = Employee("raz", 20, 10000)
emp.details()