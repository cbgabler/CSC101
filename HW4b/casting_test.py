import cast
import data


eye_point = data.Point(0.0, 0.0, -14.0)
sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1)),
               data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1, 0, 0))]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eye_point, sphere_list, data.Color(1, 1, 1))
