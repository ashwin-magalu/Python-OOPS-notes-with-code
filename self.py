class Employee:
    companyName = "ABC LLC"

    def employeeData(self):
        self.name = "Ashwin" # this is a global scoped variable
        print(self.name) # Ashwin
        salary = 5_000 # this is a local scoped variable
        print(salary) # 5000


ashwin = Employee()
ashwin.employeeData()