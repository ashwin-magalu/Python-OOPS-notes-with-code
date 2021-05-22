class BMI:
    """ This is encapsulation / hidden algorithm """
    def calculateBMI(self):
        print("\nEnter your height in meters")
        self.height = float(input())
        print("\nEnter your weight in KGs")
        self.weight = float(input())
        self.bmi = self.weight / (self.height**2)
        print(f"\nYour bmi is {self.bmi}\n")

        if self.bmi < 18.5:
            print("You are underweight\n")
        elif self.bmi > 18.5 and self.bmi < 24.9:
            print("You are healthy\n")
        elif self.bmi > 24.9 and self.bmi < 29.9:
            print("You are overweight\n")
        elif self.bmi > 29.9:
            print("You are obese\n")

bmi = BMI()

while True:
    """ This is abstraction or interface """
    print("1. Calculate your BMI")
    print("2. Exit")

    choice = int(input())

    if choice is 1:
        bmi.calculateBMI()
    elif choice is 2:
        exit()