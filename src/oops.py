class Animal:
    an_type = "Animal"

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"-- sleeping now : {self.name}")


animal1 = Animal("Max Dog")
animal1.sleep()


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def eat(self):
        print(f" -- eating -- {self.name}")


c1 = Cat("John", 40)
c1.sleep()
c1.eat()

c1.an_type = "Afsfa"
print(c1.an_type)

Animal.an_type = "Birds"
print(c1.an_type)

c2 = Cat("Warner", 45)
print(c2.an_type)


class Employee:
    company = "OpenAI"  # static variable
    count = 0  # static variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # instance
        self._bonus = 5000  # protected
        self.__secret_code = "EMP"  # private
        Employee.count += 1

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    @classmethod
    def total_employees(cls):
        return cls.count


e1 = Employee("Sachin", 10000)
print(e1.salary)
print(e1._bonus)

# private variables can't be accessed outside
print(
    e1.__secret_code
)  # AttributeError: 'Employee' object has no attribute '__secret_code'
print(e1._Employee__secret_code)  # using name Mangled we can access

print(e1.total_employees())
