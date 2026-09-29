from Shape import Shape

class RectangleOne(Shape):

    def __init__(self, name="Unknown", color = "Unkonwn", length =0, width =0):

        super().__init__(name,color)
        self.length = length
        self.width = width

    def area(self):

        return f"Area: {self.width*self.length}"

    def perimeter(self):

        return f"Perimeter: {2*(self.width+self.length)}"

r1 = RectangleOne("Rectangle", "Blue", 10, 5)
print(r1)
print(r1.area())
print(r1.perimeter())