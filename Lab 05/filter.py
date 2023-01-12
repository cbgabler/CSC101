
def are_positive(my_list):
    positive = []
    for i in my_list:
        if i > 0:
            positive.append(i)
    return positive

def are_greater_than(a, x):
    return sorted(i for i in a if i >= x)

def are_in_first_quadrant(p):
   result = []
   for i in p:
       if i.x >= 0 and i.y >= 0:
           result.append(i)
   return result
