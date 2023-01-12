import math
import data
import vector_math
import utility


def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center), 2), ray.dir)
   c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),
                              vector_math.difference_point(ray.pt, sphere.center)) - (sphere.radius ** 2)

   if b**2 - (4*a*c) < 0:
      return data.Point(0, 0, 0)

   t1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
   t2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
   if t1 < 0 and t2 < 0:
      return data.Point(0, 0, 0)

   elif t1 < 0 and t2 > 0:
      return vector_math.translate_point(vector_math.scale_vector(ray.dir, t2), ray.pt)

   elif t1 > 0 and t2 < 0:
      return vector_math.translate_point(vector_math.scale_vector(ray.dir, t1), ray.pt)

   else:
      return vector_math.translate_point(vector_math.scale_vector(ray.dir, min(t1, t2)), ray.pt)


def find_intersection_points(sphere_list, ray):
   intersection_list = []
   for f in sphere_list:
      intersect = sphere_intersection_point(ray, f)
      if intersect != data.Point(0, 0, 0):
        intersection_list.append((f, intersect))
   return intersection_list


def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
