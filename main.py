from Shape import Circle, name_shapes

circle = Circle(1)
circle.area()
name_shapes()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Hi my name is", self.name)


animal = Animal('tim')
animal.speak()


# inheritance
class Dog(Animal):
    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour

    def bark(self):
        print("Bow wow")

    def speak(self):
        print("Hi I'm a dog, my name is", self.name, "I am", self.colour, "in colour")


dog = Dog('fred', 'white')
dog.bark()
dog.speak()


# overloading existing methods
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def print(self):
        print("x:", self.x, "y:", self.y)


p1 = Point(3, 3)
p2 = Point(3, 4)
p3 = p1 + p2
p3.print()


# classmethod and staticmethod
class Vehicle():
    vehicles = ['car', 'bike', 'truck']

    @classmethod
    def count_vehicles(cls):
        print(len(cls.vehicles))

    @staticmethod
    def honk():
        print("beep beep")


Vehicle.count_vehicles()
Vehicle.honk()
