def poly_add2(poly, poly1):
    sum = []
    sum.append(poly[0] + poly1[0])
    sum.append(poly[1] + poly1[1])
    sum.append(poly[2] + poly1[2])
    return sum

def poly_mult2(poly, poly1):
    sum = []
    sum.append(poly[2] * poly1[2])
    sum.append((poly[2] * poly1[1]) + (poly1[2] * poly[1]))
    sum.append((poly[1] * poly[1]) + (poly[2] * poly1[0] + (poly1[2] * poly[0])))
    sum.append((poly[1] * poly1[0]) + (poly1[1] * poly[0]))
    sum.append(poly[0] * poly1[0])
    return sum