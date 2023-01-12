import math

def distance(p1, p2):
    d = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    return d

def radii(r1, r2):
    r = r1 + r2
    return r

def center(c1, c2):
    c = math.sqrt((c2.x-c1.x)**2+(c2.y-c1.y)**2)
    return c


