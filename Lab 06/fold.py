import math

def add_all(input_list_sum):
    output_list_sum = 0
    for i in input_list_sum:
        output_list_sum += i
    return output_list_sum

def index_of_smallest(input_list_smallest: list):
    min_input = input_list_smallest[0]
    for i in range(0, len(input_list_smallest)):
        if input_list_smallest[i] < min_input:
            min_input = input_list_smallest[i]
        return min_input

def nearest_origin(p):
    origin = [0, 0]
    distance_close = 0
    for i in range(0, len(p)):
        distances = math.sqrt((p[i].x - origin[0])**2 + (p[i].y - origin[1])**2)
        if distance_close < distances:
            distance_close = [p[i].x, p[i].y]
            return distance_close

