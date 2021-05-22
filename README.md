# Python OOPS

## What is OOPS?

    Object Oriented Programming is a programming style that is associated with the concept of Class, Objects and various other concepts revolving around these, like Inheritance, Polymorphism, Abstraction and Encapsulation etc.

## Advantages of OOP:

    1. Reusability of code
    2. Easier to maintain
    3. OOP concepts are easy to understand
    4. Secure development since data is hidden
    5. Flexibility through polymorphism.

## Why OOP?

    There are four major benefits to object-oriented programming:
        1. Encapsulation: In OOP, you bundle code into a single unit where you can determine the scope of each piece of data.
        2. Abstraction: By using classes, you are able to generalize your object types, simplifying your program.
        3. Inheritance: Because a class can inherit attributes and behaviors from another class, you are able to reuse more code.
        4. Polymorphism: One class can be used to create many objects, all from the same flexible piece of code.
    Object-oriented programming (OOP) is a programming paradigm that allows you to package together data states and functionality to modify those data states, while keeping the details hidden away. As a result, code with OOP design is flexible, modular, and abstract. This makes it particularly useful when you create larger programs.

## Classes

    1. Classes provide a means of bundling data and functionality together
    2. Creating a new class creates a new type of object.

## Object

    1. An object (instance) is an instantiation of a class
    2. An instance or object is a specific object created from a particular class.

## Creating a class

    To create a class we use 'class' keyword.
        Syntax: class Calculator:

## Instance attributes

    1. All classes create objects, and all objects contain characteristics called attributes
    2. Use the __init__() method to initialize instance attributes.
        For example:
            An employee has attributes like name, age, salary, mobile no, address, etc.,

## Class attributes

    While instance attributes are specific to each object, class attributes are the same for all instances.
        For example:
            An employee has class attributes like company name.

## Instance methods

    1. These are defined inside a class and are used to get the content of an instance
    2. These can also be used to perform operations with the attributes of our objects.

## Static methods

    1. These are created using @staticmethod decorator
    2. The @staticmethod is a built-in decorator in Python, which defined a static method
    3. A static method doesn't receive any reference argument (like self) whether it is called by an instance of a class or by the class itself
    4. These can be called directly using class-name, instead of instance-name. Because, this doesn't contain any private data.

## init method

    1. The __init__() method is called as an object of a class as instantiated or created
    2. The method is useful to do any initialization, means passing initial values to your object
    3. We do not explicitly call this method. This is like a constructor in Java.

## self parameter

    1. Class methods have only one specific difference from ordinary functions - they must have an extra parameter
    2. This particular variable refers to the object itself.
        Example:
            When you call a method like:
                obj.add(num1, num2)
            this is automatically converted by Python into:
                Calculator.add(obj, num1, num2)

        ashwin = Employee("Ashwin",27,30_000) ==> Employee.__init__(ashwin,"Ashwin",27,30_000)

## Encapsulation and Abstraction

    Encapsulation:
        1. This is the packing of data and functions into a single component and restricting the access to some of the object's components
        2. Hiding the implementation from the outside world is called encapsulation.
        For example:
            Class

    Abstraction:
        1. This refers to providing only essential information about the data to the outside world (interface for user to interact with our data)
        2. It is the process to achieve Encapsulation.
        For example:
            Google search box, this only shows a search box to outside world, algorithm behind searching is not shown to the outside world.

    Go through, bmi.py for more details.

## Inheritance (Important)

    Inheritance is the capability of one class to derive or inherit the properties from some another class.

    Advantages of Inheritance:
        1. It represents real-world relationships well
        2. It provides reusability of a code. We don't have to write the same code again and again.

### Single Inheritance

    Go through, singleinheritance.py for more details.

### Multi Level Inheritance

    Go through, multilevelinheritance.py for more details.

### Multiple Inheritance

    Go through, multipleiheritance.py for more details.

## Diamond Shape Problem in Multiple Inheritance

    Go through, diamond.py for more details.

## Access Specifiers

    Basically, there are three access specifiers:
        1. Public:
            Public member of the class can be accessed from anywhere in the program.
        2. Protected:
            Protected member of the class can be accessed only by the child classes. we add '_' (underscore) before the attribute or method-name to make it protected. Like _age or _getAge().
        3. Private:
            Private member of the class can be accessed only within that class. we add '__' (double underscores) before the attribute or method-name to make it private. Like __age or __getAge().

    Go through, access.py for more details.

## Polymorphism and Function Overriding

    1. Polymorphism means the ability to take various forms.
    2. In Python, Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

    Go through, overriding.py for more details.

## super() method

    The super function in Python can be used to gain access to inherited methods which is either from the parent class or sibling class.

    Go through, overriding.py for more details.

## Function Overloading

    Function overloading means, that we create different versions of function in the same class. This is not supported in Python, we can write function overloading methods. But that is not right.

    Go through, overloading.py for more details.

## Operator Overloading

    Go through, operatoroverloading.py for more details.

## Clearing concepts of Abstract classes and Abstract methods

    Go through, abstract.py for more details.