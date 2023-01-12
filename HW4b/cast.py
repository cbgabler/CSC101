import collisions
import vector_math
import data
import unittest


def cast_ray(ray, sphere_list, color):
    collisions_list = collisions.find_intersection_points(sphere_list, ray)
    if collisions_list:
        smallest_dist = vector_math.length_vector(vector_math.difference_vector(collisions_list[0][1], ray.pt))
        sphere = collisions_list[0][0]
        for i in range(len(collisions_list)):
            if vector_math.length_vector(vector_math.difference_vector(collisions_list[i][1], ray.pt)) < smallest_dist:
                smallest_dist = vector_math.length_vector(vector_math.difference_vector(collisions_list[i][1], ray.pt))
                sphere = collisions_list[i][0]
        r = 0
        g = 0
        b = 0

        # find the correct color of the spheres, shadows, and finishes
        r = r + sphere.color.r*color.r
        g = g + sphere.color.g*color.g
        b = b + sphere.color.b*color.b

        # cases if color values > 1
        if r > 1:
            r = 1
        if g > 1:
            g = 1
        if b > 1:
            b = 1

        return data.Color(r, g, b)
    else:
        return data.Color(1, 1, 1)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color):
    print('P3')
    print(width, height)
    print('255')

    x_calc = (max_x - min_x)/float(width)
    y_calc = (max_y - min_y)/float(height)
    for h in range(height):
        for w in range(width):
            x = min_x + x_calc * w
            y = max_y - y_calc * h
            z = 0
            ray = data.Ray(eye_point, vector_math.difference_point(data.Point(x, y, z), eye_point))
            color_output = cast_ray(ray, sphere_list, color)
            print(str(int(color_output.r*255)) + " " + str(int(color_output.g*255)) + " " +
                  str(int(color_output.b*255)))


if __name__ == '__main__':
    unittest.main()
