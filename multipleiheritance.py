""" Multiple Inheritance """

class Person:
    """ Parent class """
    name = "Bob"
    gender = "Male"

class Student(Person):
    """ Intermediate level class """
    fees = 15_000
    age = 30

class Faculty(Person):
    """ Intermediate level class """
    salary = 5_000
    lunch = False
    bonus = True
    age = 40

class TA(Student, Faculty):
    """ Child class """
    def showTAData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}") 
        # 30 --> order matters, when two classes have same attributes, whatever comes 1st is printed
        print(f"Gender: {self.gender}")
        print(f"Fees: {self.fees}")
        print(f"Lunch: {self.lunch}")
        print(f"Bonus: {self.bonus}")
        print(f"Salary: {self.salary}\n")


ta = TA()
ta.showTAData()