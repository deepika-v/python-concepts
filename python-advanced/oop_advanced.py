"""
OOP Advanced Concepts

This file demonstrates:
- Abstract Base Classes (abc)
- Multiple inheritance behavior and pitfalls
- Composition versus inheritance
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Multiple inheritance example
class Animal:
    def speak(self):
        return "generic sound"


class Walker:
    def walk(self):
        return "walking"


class Flyer:
    def walk(self):
        return "flying"


class Bird(Animal, Walker, Flyer):
    def speak(self):
        return "chirp"


def demonstrate_multiple_inheritance():
    print("=== Multiple Inheritance and MRO ===")
    bird = Bird()
    print("Bird speak:", bird.speak())
    print("Bird walk:", bird.walk())
    print("MRO:", [cls.__name__ for cls in Bird.__mro__])
    print("Note: The left-to-right order of inheritance affects which method is used.")


# Composition vs Inheritance
class Engine:
    def start(self):
        return "Engine started"


class CarInheritance(Engine):
    def drive(self):
        return f"Driving with {self.start()}"


class CarComposition:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return f"Driving with {self.engine.start()}"


def demonstrate_composition_vs_inheritance():
    print("=== Composition vs Inheritance ===")
    inherited_car = CarInheritance()
    composed_car = CarComposition()
    print("Inheritance:", inherited_car.drive())
    print("Composition:", composed_car.drive())
    print(
        "Composition keeps responsibilities separate and is often easier to extend or mock."
    )


def main():
    print("OOP Advanced Demonstration")
    print("=" * 30)
    circle = Circle(5)
    rectangle = Rectangle(3, 6)
    for shape in (circle, rectangle):
        print(f"{shape.__class__.__name__}: area={shape.area()}, perimeter={shape.perimeter()}")
    print()
    demonstrate_multiple_inheritance()
    print()
    demonstrate_composition_vs_inheritance()


if __name__ == "__main__":
    main()