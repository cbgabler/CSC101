import unittest
import cast
import data

spherelist = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2), data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5)]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.Point(0.0, 0.0, -14.0), spherelist)
