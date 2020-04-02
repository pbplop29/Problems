class Circle(object):
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return ((int(self.radius))**2) * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def perimeter(self):
        return((int(self.radius)*2*Circle.pi))

    def get_radius(self):
        return self.radius


c = Circle(radius=5)
print(c.pi)
print(c.radius)
print(str(c.area()) + " m")
print(str(c.perimeter()) + " m")

c.set_radius(10)
print(c.pi)
print(c.radius)
print(str(c.area()) + " m")
print(str(c.perimeter()) + " m")

print(c.radius)

c.set_radius(20)
print(c.radius)

print(c.get_radius())
