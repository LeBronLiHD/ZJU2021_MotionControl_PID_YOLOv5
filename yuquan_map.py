# -*- coding: utf-8 -*-

"""
Map of Yuquan campus -> graph
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from dijkstra import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point ->", self.x, self.y)


class Vector:
    def __init__(self, p1, p2, p1_num, p2_num):
        self.p1 = p1
        self.p2 = p2
        self.length = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        self.p1_num = p1_num
        self.p2_num = p2_num

    def show(self):
        print("Vector -> (" +
              str(self.p1.x) + "," + str(self.p1.y) + ") -> (" +
              str(self.p2.x) + "," + str(self.p2.y) + ")")


class Graph:
    def __init__(self, v, e, vectors, points):
        self.v = v
        self.e = e
        self.vectors = vectors
        self.points = points

    def show(self):
        print("number of vertices ->", self.v)
        print("number of edges ->", self.e)
        for vector in self.vectors:
            vector.show()

    def check_vex_edge(self):
        vexnum, edge = self.v, self.e
        if vexnum <= 0 or edge <= 0 or (vexnum * (vexnum - 1))/2.0 < edge:
            return False
        else:
            return True


def build_graph():
    X = [98, 96, 94, 82, 107, 116, 113, 105, 84, 83,
         88, 84, 92, 100, 110, 118, 108, 107, 117, 106,
         104, 95, 96, 95, 82, 114, 127, 112, 121, 120,
         111, 117, 107, 103, 99, 96, 79, 77, 69, 72,
         64, 59, 73, 86, 89, 97, 102, 114, 117, 113,
         108, 100, 38, 45, 49, 53, 53, 62, 65, 68,
         87, 98, 102, 108, 114, 107, 100, 103, 101, 95,
         85, 66, 63, 61, 51, 48, 43, 38, 30, 24,
         19, 16, 21, 28, 22, 42, 41, 59, 67, 84,
         93, 75, 73, 66, 88, 72, 63, 55, 49, 38,
         32, 35, 41, 46, 48, 53, 51, 60, 68, 71,
         77, 83, 81, 80, 76, 68, 69, 67, 63, 48,
         46, 55, 50]
    Y = [167, 157, 152, 163, 151, 148, 136, 140, 144, 136,
         131, 118, 133, 130, 129, 126, 122, 119, 115, 111,
         105, 118, 112, 108, 112, 105, 98, 100, 96, 90,
         95, 76, 82, 94, 89, 97, 104, 98, 100, 116,
         118, 108, 87, 81, 87, 83, 67, 60, 54, 54,
         55, 60, 82, 80, 78, 71, 66, 65, 64, 63,
         55, 50, 46, 44, 40, 36, 40, 32, 24, 43,
         49, 56, 61, 65, 58, 60, 62, 65, 68, 60,
         65, 63, 59, 56, 57, 53, 50, 47, 46, 44,
         38, 43, 39, 42, 31, 35, 38, 40, 40, 41,
         50, 36, 32, 33, 38, 35, 30, 29, 26, 24,
         22, 20, 15, 10, 17, 14, 20, 21, 16, 20,
         15, 24, 25]
    num_v = len(X)
    plt.figure(figsize=(9, 12))
    plt.scatter(X, Y, c=np.random.rand(num_v), alpha=1.0)  # edgecolors='b'
    for i in range(num_v):
        text_kwargs = dict(ha='center', va='bottom',
                           fontfamily='monospace', fontsize=10, color='black')
        plt.text(X[i], Y[i], str(i + 1), **text_kwargs)
    plt.title("Yuquan Campus")
    E1 = [62, 61, 43, 61, 66, 66, 64, 50, 21, 21, 21, 1, 2, 2, 5, 3, 5, 6, 8, 7, 15, 15, 16, 14, 13, 9, 3, 10, 11, 7, 18, 18, 23,
          20, 18, 20, 21, 26, 12, 26,
          28, 28, 30, 28, 30, 32, 32, 33, 33, 34, 24, 24, 36, 36, 25, 36, 34, 38, 38, 40, 40, 42, 42, 43, 43, 45, 45,
          46, 33, 48, 47,
          48, 51, 47, 52, 52, 62, 57, 59, 59, 61, 54, 54, 56, 56, 70, 70, 63, 63, 65, 64, 67, 69, 70, 71, 71,
          73, 74, 57, 58, 72, 75, 77, 77, 79, 79, 78, 91, 90, 90, 91, 88, 92, 88, 88, 77, 87, 80, 83, 81, 84, 84, 85,
          84, 93, 93, 96, 89, 97, 96, 98, 98, 100, 100, 102, 99, 99, 112, 106, 108, 108, 110, 110, 112, 112, 114, 102,
          104, 104, 106, 104, 123, 107, 122, 108, 109, 120, 121, 109, 118, 110, 115, 118, 120, 116, 114]
    E2 = [63, 71, 59, 46, 67, 65, 51, 49, 23, 24, 28, 2, 3, 5, 6, 4, 8, 7, 14, 15, 16, 17, 19, 17, 14, 10, 11, 11, 12, 8, 17, 19,
          12, 22, 20, 21, 26, 19, 25,
          27, 26, 29, 29, 31, 31, 30, 33, 31, 34, 21, 23, 25, 24, 37, 37, 35, 35, 37, 39, 39, 41, 41, 55, 38, 44, 44,
          46, 35, 47, 32, 48, 50, 50, 52, 51, 62, 61, 58, 58, 60, 60, 53, 55, 55, 57, 62, 67, 67, 64, 64, 66,
          68, 68, 91, 70, 72, 72, 75, 75, 74, 60, 76, 76, 77, 78, 80, 54, 95, 71, 92, 90, 89, 89, 73, 86, 86, 86, 83,
          82, 83, 79, 83, 84, 87, 92, 96, 95, 94, 94, 97, 88, 106, 87, 101, 100, 100, 98, 95, 107, 107, 109, 109, 111,
          111, 113, 113, 103, 103, 105, 105, 107, 104, 123, 123, 97, 96, 123, 120, 118, 117, 117, 111, 119, 119, 117,
          116]
    print("points ->", len(X), len(Y))
    print("vectors ->", len(E1), len(E2), max(E1), max(E2), min(E1), min(E2))
    num_v = len(X)
    num_e = len(E1)
    points = []
    for i in range(num_v):
        points.append(Point(X[i], Y[i]))
    for i in range(num_e):
        plt.plot([points[E1[i] - 1].x, points[E2[i] - 1].x],
                 [points[E1[i] - 1].y, points[E2[i] - 1].y], linewidth=2.5)
    plt.show()
    vectors = []
    for i in range(num_e):
        vectors.append(Vector(points[E1[i]], points[E2[i]], E1[i], E2[i]))
    G = Graph(num_v, num_e, vectors=vectors, points=points)
    if G.check_vex_edge() is False:
        print("Graph invalid! Check the relation of vex_num and edge_num!")
    return G


def search_path(G, start, dest):
    Graph.Dijkstra(start)
    Graph.printPath(start)
    distance = Graph.searchPath(dest)
    return distance


def draw_path(G, distance):
    X, Y = [], []
    for point in G.points:
        X.append(point.x)
        Y.append(point.y)
    plt.figure(figsize=(9, 12))



if __name__ == '__main__':
    G = build_graph()
    G.show()
    # Graph = GraphDijkstra(G.v, G.e)
    # Graph.createGraphEgeds(G.vectors)
    # Graph.printGraph()
    # print("Input start and dest: ", end="")
    # start, dest = map(int, input().split())
    # distance = search_path(Graph, start, dest)
    # draw_path(G, distance)
