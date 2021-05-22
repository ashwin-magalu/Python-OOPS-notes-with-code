""" Multi Level Inheritance """

class Person:
    """ Parent class """
    name = "Bob"
    age = 40
    gender = "Male"

class Student(Person):
    """ Intermediate level class """
    fees = 15_000

class TA(Student):
    """ Child class """
    salary = 5_000

    def showTAData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"fees: {self.fees}")
        print(f"Salary: {self.salary}\n")

ta = TA()
ta.showTAData()