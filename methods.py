class Employee:
    companyName = "ABC LLC" # class attribute
    
    def __init__(self, name, age, salary):
        """ Using instance attributes here """
        self.name = name
        self.age = age
        self.salary = salary

    def showEmployeeDetails(self):
        """ Instance method """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.companyName}")

    @staticmethod
    def getCompanyInfo():
        """ static method """
        print("This company was founded in the early 2000s")

ashwin = Employee("Ashwin", 27, 20_000)
ashwin.getCompanyInfo() # This company was founded in the early 2000s
Employee.getCompanyInfo() # This company was founded in the early 2000s