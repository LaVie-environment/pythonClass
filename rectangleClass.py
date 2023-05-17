
class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.breath = right_lower[0] - left_upper[0]
        self.length = right_lower[1] - left_upper[1]

    def area(self):
        return self.length * self.breath

    def perimeter(self):
        return self.length * 2 + self.breath * 2

    def move(self, x_change: int, y_change: int):
        corner = self.left_upper
        self.left_upper = (corner[0]+x_change, corner[1]+y_change)
        corner = self.right_lower
        self.right_lower = (corner[0]+x_change, corner[1]+y_change)


rectangle = Rectangle((1,1), (4,3))
print(rectangle.area())

    