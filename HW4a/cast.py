import collisions
import data
import vector_math

def cast_ray(ray, sphere_list):
    if collisions.find_intersection_points(sphere_list, ray):
        return True
    else:
        return False

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    print('P3')
    print(width, height)
    print('255')

    x_calc = (max_x - min_x)/width
    y_calc = (max_y - min_y)/height

    for n in range(height):
        for i in range(width):
            x = min_x + i * x_calc
            y = max_y - n * y_calc
            plane_point = data.Point(x, y, 0)
            vector_to_ray = vector_math.vector_from_to(eye_point, plane_point)
            if cast_ray(data.Ray(eye_point, vector_to_ray), sphere_list):
                print('0 0 0')
            else:
                print('200 200 200')