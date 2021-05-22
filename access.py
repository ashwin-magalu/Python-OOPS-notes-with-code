class Employee:
    name = "Ashwin" # public member
    _age = 27 # protected member
    __salary = 10_000 # private member --> converted to _Employee__salary

    def showEmpData(self):
        print(f"Salary: {self.__salary}")

class Test(Employee):
    def showData(self):
        print(f"Age: {self._age}")
        # print(f"Salary: {self.__salary}") # error

ashwin = Employee()
print(ashwin.name)
print(ashwin._age)
# print(ashwin.__salary) # error
print(ashwin._Employee__salary) # no error, this way we can access private variable
t = Test()
t.showData()
ashwin.showEmpData()

""" Python don't have private or protected, we use these naming conventions to make the members private, public or protected """