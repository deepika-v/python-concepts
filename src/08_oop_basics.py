"""
Python Object-Oriented Programming (OOP) Concepts

This module demonstrates:
- Classes and objects
- Attributes and methods
- Constructors (__init__)
- Inheritance
- Encapsulation (public, protected, private)
- Polymorphism
- Special methods (dunder methods)
"""

# ============================================================================
# BASIC CLASS AND OBJECT
# ============================================================================

print("=" * 60)
print("BASIC CLASS AND OBJECT")
print("=" * 60)

class Dog:
    """A simple Dog class."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor - called when object is created."""
        self.name = name  # Instance attribute
        self.age = age
    
    def bark(self):
        """Instance method."""
        return f"{self.name} says Woof!"

# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.name}, Age: {dog1.age}")
print(f"Dog 2: {dog2.name}, Age: {dog2.age}")
print(f"Species: {Dog.species}")
print(dog1.bark())

# ============================================================================
# INSTANCE vs CLASS ATTRIBUTES
# ============================================================================

print("\n" + "=" * 60)
print("INSTANCE vs CLASS ATTRIBUTES")
print("=" * 60)

class Counter:
    """Class to demonstrate instance vs class attributes."""
    count = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute
        Counter.count += 1

c1 = Counter("Object1")
c2 = Counter("Object2")
c3 = Counter("Object3")

print(f"c1.name: {c1.name}, Counter.count: {Counter.count}")
print(f"c2.name: {c2.name}, Counter.count: {Counter.count}")
print(f"c3.name: {c3.name}, Counter.count: {Counter.count}")

# ============================================================================
# METHODS
# ============================================================================

print("\n" + "=" * 60)
print("METHODS")
print("=" * 60)

class Calculator:
    """Calculator class to demonstrate different method types."""
    
    pi = 3.14159  # Class constant
    
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        """Instance method - requires self."""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method - doesn't need self."""
        return a * b
    
    @classmethod
    def from_dict(cls, data):
        """Class method - receives class as first argument."""
        return cls(data['name'])
    
    def __str__(self):
        """Special method - string representation."""
        return f"Calculator: {self.name}"

calc = Calculator("MyCalc")
print(f"Add: {calc.add(5, 3)}")
print(f"Multiply: {Calculator.multiply(4, 6)}")
print(f"String repr: {calc}")

# ============================================================================
# INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("INHERITANCE")
print("=" * 60)

class Animal:
    """Base class (parent class)."""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    """Derived class (child class) - inherits from Animal."""
    
    def speak(self):
        """Override parent method."""
        return f"{self.name} meows"

class Bird(Animal):
    """Another derived class."""
    
    def speak(self):
        return f"{self.name} chirps"

# Create instances
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(f"Cat: {cat.speak()}")
print(f"Bird: {bird.speak()}")

# ============================================================================
# SUPER() FUNCTION
# ============================================================================

print("\n" + "=" * 60)
print("SUPER() FUNCTION - ACCESSING PARENT CLASS")
print("=" * 60)

class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    """Car class inheriting from Vehicle."""
    
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
    
    def start(self):
        """Override and extend parent method."""
        parent_msg = super().start()
        return f"{parent_msg} - Car model: {self.model}"

car = Car("Toyota", "Camry")
print(car.start())

# ============================================================================
# MULTIPLE INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("MULTIPLE INHERITANCE")
print("=" * 60)

class Flyable:
    """Mixin class for flying capability."""
    
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class for swimming capability."""
    
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from multiple classes."""
    pass

duck = Duck("Donald")
print(duck.speak())
print(duck.fly())
print(duck.swim())

# ============================================================================
# ENCAPSULATION (PRIVATE AND PROTECTED ATTRIBUTES)
# ============================================================================

print("\n" + "=" * 60)
print("ENCAPSULATION - DATA HIDING")
print("=" * 60)

class BankAccount:
    """Bank account with private attributes."""
    
    def __init__(self, balance):
        self._balance = balance  # Protected (single underscore)
        self.__pin = "1234"      # Private (double underscore)
    
    def get_balance(self):
        """Getter method."""
        return self._balance
    
    def deposit(self, amount):
        """Public method to modify private attribute."""
        if amount > 0:
            self._balance += amount
            return f"Deposited: {amount}"
        return "Invalid amount"
    
    def withdraw(self, amount, pin):
        """Method requiring PIN to access."""
        if pin == self.__pin and amount <= self._balance:
            self._balance -= amount
            return f"Withdrawn: {amount}"
        return "Invalid PIN or insufficient funds"

account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200, "1234"))
print(f"Balance: {account.get_balance()}")

# ============================================================================
# POLYMORPHISM
# ============================================================================

print("\n" + "=" * 60)
print("POLYMORPHISM")
print("=" * 60)

class Shape:
    """Base shape class."""
    
    def area(self):
        pass

class Circle(Shape):
    """Circle class."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    """Rectangle class."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")

# ============================================================================
# SPECIAL METHODS (DUNDER METHODS)
# ============================================================================

print("\n" + "=" * 60)
print("SPECIAL METHODS (DUNDER METHODS)")
print("=" * 60)

class Person:
    """Person class with special methods."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly string representation."""
        return f"Person: {self.name}, {self.age} years old"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """Return length (for len())."""
        return self.age
    
    def __eq__(self, other):
        """Equality comparison."""
        return self.age == other.age
    
    def __lt__(self, other):
        """Less than comparison."""
        return self.age < other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(f"__str__: {str(p1)}")
print(f"__repr__: {repr(p1)}")
print(f"__len__: len(p1) = {len(p1)}")
print(f"__eq__: p1 == p2 = {p1 == p2}")
print(f"__lt__: p1 < p2 = {p1 < p2}")

# ============================================================================
# ABSTRACT BASE CLASS
# ============================================================================

print("\n" + "=" * 60)
print("ABSTRACT BASE CLASS")
print("=" * 60)

from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract base class."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_salary(self):
        """Abstract method - must be implemented by subclasses."""
        pass

class Manager(Employee):
    """Concrete implementation."""
    
    def __init__(self, name, base_salary):
        super().__init__(name)
        self.base_salary = base_salary
    
    def calculate_salary(self):
        """Implement abstract method."""
        return self.base_salary * 1.2  # 20% bonus

manager = Manager("John", 5000)
print(f"Manager {manager.name} salary: {manager.calculate_salary()}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Class: Blueprint for objects
2. Instance: An object created from a class
3. __init__: Constructor method
4. self: Refers to the instance
5. Instance attribute: Unique to each object
6. Class attribute: Shared by all instances
7. Instance method: Operates on instance
8. Static method: Doesn't need self
9. Class method: Operates on class
10. Inheritance: Derive classes from parent
11. super(): Access parent class methods
12. Encapsulation: Hide internal data
13. Polymorphism: Different classes, same method name
14. Dunder methods: __str__, __repr__, __eq__, etc.
15. ABC: Abstract Base Class for interface definition
""")
