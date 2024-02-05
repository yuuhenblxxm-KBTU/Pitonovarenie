class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point1.move(4, 6)
point1.show()

distance = point1.dist(point2)
print("Distance =", distance)
