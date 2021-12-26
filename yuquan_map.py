# -*- coding: utf-8 -*-

"""
Map of Yuquan campus -> graph
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point ->", self.x, self.y)


class Vector:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.length = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def show(self):
        print("Vector -> (" + self.p1.x + "," + self.p1.y + ") -> (" + self.p2.x + "," + self.p2.y + ")")


class Graph:
    def __init__(self, v, e, vectors):
        self.v = v
        self.e = e
        self.vectors = vectors

    def show(self):
        print("number of vertices ->", self.v)
        print("number of edges ->", self.e)
        for vector in self.vectors:
            vector.show()


def build_graph():
    num_v = 123
    num_e = 123
    X = [98, 96, 94, 89, 107, 116, 112, 104, 84, 83,
         88, 84, 92, 100, 110, 118, 108, 107, 117, 106,
         104, 97, 96, 95, 83, 113, 132, 112, 123, 122,
         111, 119, 107, 103, 94, 93, 81, 78, 71, 72,
         67, 61, 73, 85, 88, 92, 102, 114, 116, 112,
         108, 100, 38, 45, 49, 53, 53, 62, 65, 67,
         81, 96, 102, 108, 113, 104, 100, 103, 101, 94,
         78, 65, 63, 61, 51, 48, 43, 38, 30, 24,
         19, 16, 21, 28, 22, 42, 41, 59, 67, 76,
         91, 75, 73, 66, 88, 72, 63, 55, 49, 38,
         32, 35, 41, 46, 48, 53, 51, 60, 68, 71,
         77, 83, 81, 80, 76, 68, 69, 67, 63, 48,
         46, 55, 50]
    Y = [167, 157, 152, 158, 151, 148, 131, 139, 144, 136,
         131, 118, 133, 130, 129, 126, 122, 119, 115, 111,
         119, 115, 112, 116, 108, 101, 104, 100, 96, 99,
         84, 88, 94, 94, 100, 110, 104, 108, 114, 116,
         110, 90, 87, 89, 88, 71, 67, 66, 63, 61,
         64, 85, 82, 80, 78, 71, 66, 65, 64, 59,
         54, 51, 47, 44, 45, 46, 34, 30, 48, 53,
         59, 59, 61, 65, 58, 60, 62, 65, 68, 60,
         65, 63, 59, 56, 57, 53, 50, 47, 46, 41,
         44, 43, 39, 42, 31, 35, 38, 40, 40, 41,
         50, 36, 32, 33, 38, 35, 30, 29, 26, 24,
         22, 20, 15, 10, 17, 114, 20, 21, 16, 20,
         15, 24, 25]
    points = []
    vectors = []
    E1 = []
    E2 = []
    for i in range(num_v):
        points.append(Point(X[i], Y[i]))
    for i in range(num_e):
        vectors.append(Vector(points[E1[i]], points[E2[i]]))
    G = Graph(num_v, num_e, vectors=vectors)
    return G


if __name__ == '__main__':
    G = build_graph()
    G.show()
