class Employee:
    name = "Ashwin" # instance attribute
    age = 27 # instance attribute
    salary = 10_000 # instance attribute

    def getSalary(self): 
        """ instance method """
        return self.salary

ashwin = Employee() # creates an object / instance of Employee class
print(ashwin.getSalary()) # 10000
print(ashwin.age) # 27
