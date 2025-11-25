class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.age})"
    
    def myfunc(self):
        print("HEllo my name is" + self.first_name + " " + self.last_name)


x = Person("Jhon", "Doe", 56)

class Student(Person):
    pass


s1 = Student("Tom", "Duffy" 15)



