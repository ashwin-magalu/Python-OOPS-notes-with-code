class Employee:
    companyName = "ABC LLC" # class attribute
    name = "Ashwin" # instance attribute
    age = 27 # instance attribute
    salary = 5_000 # instance attribute

""" Always object looks for the instance attribute before class attribute """

ash = Employee()
ashwin = Employee()
print(ash.companyName) # ABC LLC
print(ashwin.companyName) # ABC LLC

Employee.companyName = "XYZ LLC"
print(ash.companyName) # XYZ LLC
print(ashwin.companyName) # XYZ LLC

ash.name = "Ash"
print(ash.name) # Ash
print(ashwin.name) # Ashwin

ash.companyName = "DEF LLC"
print(ash.companyName) # DEF LLC
print(ashwin.companyName) # XYZ LLC
