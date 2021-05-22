from abc import ABC, abstractmethod

class Animal(ABC):
    """ Abstract class """
    @abstractmethod
    def whatIEat(self):
        """ abstract method """
        pass

class Lion(Animal):
    def whatIEat(self):
        print("Lion eats meat")

class Cow(Animal):
    def whatIEat(self):
        print("Cow eats grass")

class Dog(Animal):
    def whatIEat(self):
        print("Dog eats dog food and drinks milk")

class Cat(Animal):
    pass

lion = Lion()
lion.whatIEat()
cow = Cow()
cow.whatIEat()
dog = Dog()
dog.whatIEat()

# animal = Animal()
# animal.whatIEat() # Can't instantiate abstract class Animal with abstract method whatIEat

# cat = Cat() # Can't instantiate abstract class Cat with abstract method whatIEat