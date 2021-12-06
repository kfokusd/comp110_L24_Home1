import math

class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        pass

    def getPerimeter(self):
        return 0
    
    def getArea(self):
        return 0
    
    def __str__(self):
        return "Shape({:.2f}, {:.2f})".format(self._x, self._y)


class Circle(Shape):
    # TODO: Implement this class (need to override 4 methods)
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        pass        # TODO: Need to modify this code


## Do NOT change the following
shape1 = Shape(0, 0)
cir1 = Circle(1, 1, 4)

ShapeList = []
ShapeList.append(shape1)
ShapeList.append(cir1)
for shape in ShapeList:
    print(shape)


## Expected Output:
#Shape(0.00, 0.00)
#Circle(1.00, 1.00): Radius=4.00 with Area=50.27 and Perimeter=25.13