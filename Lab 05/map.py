import math

def square_all(num):
    square_num = []
    for i in num:
        square_num.append(i ** 2)
    return square_num

def add_n_all(input_list, n):
    comp_list = [input_list[x] + n for x in range(len(input_list))]
    return comp_list

def distance_all(p):
        result = []
        origin = [0, 0]
        for i in range(len(p)):
            distance = math.sqrt((p[i].x - origin[0]) ** 2 + (p[i].y - origin[1]) ** 2)
            result.append(distance)
        return result
