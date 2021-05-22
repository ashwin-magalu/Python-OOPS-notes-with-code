class Employee:
    companyName = "ABC LLC"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def showEmployeeDetails(this):
        """ we can call 'self' as anything we want. Here, I called it as 'this'. But call it as 'self' itself as it is the standard way """
        print(f"\nName: {this.name}")
        print(f"Age: {this.age}")
        print(f"Salary: {this.salary}")
        print("Company:", this.companyName)

ashwin = Employee("Ashwin", 27, 30_000)
ashwin.showEmployeeDetails()
ash = Employee("Ash", 25, 20_000)
ash.showEmployeeDetails()