""" Single Inheritance """

class Person:
    """ Parent class """
    def setData(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(Person):
    """ Child class """
    def __init__(self, salary):
        self.salary = salary

    def showTeacherData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Salary: {self.salary}\n")

class Student(Person):
    """ Child class """
    def __init__(self, fees):
        self.fees = fees

    def showStudentData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Fees: {self.fees}\n")

teacher = Teacher(9_000)
teacher.setData("Bob", 30, "Male")
teacher.showTeacherData()

student = Student(15_000)
student.setData("Marie", 12, "Female")
student.showStudentData()