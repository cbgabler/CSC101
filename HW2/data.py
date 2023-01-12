import utility


class Point:
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def __eq__(self, other):
        x = utility.epsilon_equal(self.x, other.x)
        y = utility.epsilon_equal(self.y, other.y)
        z = utility.epsilon_equal(self.z, other.z)
        return x and y and z


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        x1 = utility.epsilon_equal(self.x, other.x)
        y1 = utility.epsilon_equal(self.y, other.y)
        z1 = utility.epsilon_equal(self.z, other.z)
        return x1 and y1 and z1


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pt1 = Point.__eq__(self.pt, other.pt)
        dir1 = Vector.__eq__(self.dir, other.dir)
        return pt1 and dir1


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        center1 = Point.__eq__(self.center, other.center)
        radius1 = utility.epsilon_equal(self.radius, other.radius)
        return center1 and radius1
