from abc import ABC, abstractmethod
import math

class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

    def describe(self):
        params = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        print(f"{self.__class__.__name__}({params})")


class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * (self.side ** 2)


class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)


shapes = [
    Cube(2),
    Sphere(3),
    Cylinder(2, 5)
]

for s in shapes:
    s.describe()
    print("Volume:", round(s.volume(), 2))
    print("Surface area:", round(s.surface_area(), 2))
    print("---")

