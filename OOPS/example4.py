#Code to find area of recatngle using inhertance and method overriding.
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print(f"The area of the rectangle is: {rectangle.area()}")