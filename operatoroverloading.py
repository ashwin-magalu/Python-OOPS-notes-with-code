""" print(1 + 2)
print("A" + "B") """
""" Here, + is an overloaded operator. Because, it has to add when it is a number on both sides and it has to concatenate if both sides are strings or if one side is string """

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        """ operator overloading method, __add__ is python's internal method to add, __sub__ for subtraction, etc., """
        return self.num1 + other.num1, self.num2 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num1, self.num2 - other.num2


obj1 = Calculator(3, 7)
obj2 = Calculator(4, 2)
obj3 = obj1 + obj2
print(obj3) 
# without __add__(): error --> unsupported operand type(s) for +: 'Calculator' and 'Calculator', with __add__(): output -> (7,9)

obj4 = obj1 - obj2
print(obj4) # (-1, 5)
