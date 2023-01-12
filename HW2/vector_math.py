import data
import math

def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    return data.Vector(x, y, z)

def dot_vector(vector1, vector2):
    x = (vector1.x * vector2.x)
    y = (vector1.y * vector2.y)
    z = (vector1.z * vector2.z)
    dotvec = x + y + z
    return dotvec

def length_vector(vector):
    vector_length = math.sqrt((vector.x**2)+(vector.y**2)+(vector.z**2))
    return vector_length

def normalize_vector(vector):
    x = (vector.x/length_vector(vector))
    y = (vector.y/length_vector(vector))
    z = (vector.z/length_vector(vector))
    return data.Vector(x, y, z)

def difference_point(point1, point2):
    point1.x = (point1.x - point2.x)
    point1.y = (point1.y - point2.y)
    point1.z = (point1.z - point2.z)
    return data.Point(point1.x, point1.y, point1.z)

def difference_vector(vector1, vector2):
    vector1.x = (vector1.x - vector2.x)
    vector1.y = (vector1.y - vector2.y)
    vector1.z = (vector1.z - vector2.z)
    return  data.Vector(vector1.x, vector1.y, vector1.z)

def translate_point(point, vector):
    point.x = (point.x + vector.x)
    point.y = (point.y + vector.y)
    point.z = (point.z + vector.z)
    return data.Point(point.x, point.y, point.z)

def vector_from_to(from_point, to_point):
    to_point.x = (to_point.x - from_point.x)
    to_point.y = (to_point.y - from_point.y)
    to_point.z = (to_point.z - from_point.z)
    return data.Vector(to_point.x, to_point.y, to_point.z)