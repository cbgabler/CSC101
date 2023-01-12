def max_101(x, y):
    return x if x > y else y

def max_of_three(x, y, z):
    if x > y & x > z:
        return x
    elif y > x & y > z:
        return y
    else:
        return z

def rental_late_fee(days):
    if days <= 0:
        return 0
    elif days <= 9:
        return 5
    elif days <= 15:
        return 7
    elif days <= 24:
        return 19
    else:
        return 100