# -*- coding: utf-8 -*-

import sys


class Distance:
    """docstring for Distance"""
    path = ""
    path_list = []
    value = 0
    visit = False

    def __init__(self):
        self.path = ""
        self.value = 0
        self.path_list = []
        self.visit = False


class GraphDijkstra:
    def __init__(self, vertex, edge):
        self.vexnum = vertex
        self.edge = edge
        self.arc = [[sys.maxsize] * vertex for _ in range(vertex)]
        self.dis = [Distance() for _ in range(vertex)]

    def refreshGraphDis(self):
        self.dis = [Distance() for _ in range(self.vexnum)]

    def refreshGraph(self):
        self.arc = [[sys.maxsize] * self.vexnum for _ in range(self.vexnum)]
        self.dis = [Distance() for _ in range(self.vexnum)]

    def checkEdgeValue(self, start, end, weight):
        if start < 1 or end < 1 or start > self.vexnum or end > self.vexnum or weight < 0:
            return False
        else:
            return True

    def createGraph(self):
        print("Input the start point, end point and weight of all edges")
        count = 0
        while count < self.edge:
            start, end, weight = map(int, input("For the " + str(count + 1) + " edge: ").split())
            while self.checkEdgeValue(start, end, weight) is False:
                print("InValid Input, Please Input Again")
                start, end, weight = map(int, input("For the " + str(count + 1) + " edge: ").split())
            self.arc[start - 1][end - 1] = weight
            count += 1

    def createGraphEgeds(self, vectors):
        for vector in vectors:
            start, end, weight = vector.p1_num, vector.p2_num, vector.length
            self.arc[start - 1][end - 1] = weight
            self.arc[end - 1][start - 1] = weight

    def printGraph(self):
        print("Linked Matrix of Graph:")
        for i in range(self.vexnum):
            for j in range(self.vexnum):
                if self.arc[i][j] == sys.maxsize:
                    print("∞", end="\t\t")
                else:
                    print(self.arc[i][j], end="\t\t")
            print("")

    def Dijkstra(self, begin):
        # 1. Initializarion
        for i in range(self.vexnum):
            self.dis[i].path = "v" + str(begin) + " --> v" + str(i + 1)
            self.dis[i].path_list.append(begin)
            self.dis[i].path_list.append(i + 1)
            self.dis[i].value = self.arc[begin - 1][i]
        self.dis[begin - 1].visit = True
        self.dis[begin - 1].value = 0
        countVisited = 1
        # 2. Other Shortest Paths
        while countVisited < self.vexnum:
            # 3. Find the Shortest and Unvisited Path
            minLength = sys.maxsize
            minIndex = 0
            for i in range(self.vexnum):
                if self.dis[i].visit is False and self.dis[i].value < minLength:
                    minLength = self.dis[i].value
                    minIndex = i
            self.dis[minIndex].visit = True
            countVisited += 1
            # 4. In Triangle, the Sun of Any Two Edges is Bigger than the Third One
            for i in range(self.vexnum):
                if self.dis[i].visit is False and \
                        self.arc[minIndex][i] != sys.maxsize and \
                        self.dis[i].value > self.arc[minIndex][i] + minLength:
                    self.dis[i].value = minLength + self.arc[minIndex][i]
                    self.dis[i].path = self.dis[minIndex].path + " --> v" + str(i + 1)
                    # self.dis[i].path_list = self.dis[minIndex].path_list
                    self.dis[i].path_list = []
                    for node in self.dis[minIndex].path_list:
                        self.dis[i].path_list.append(node)
                    self.dis[i].path_list.append(i + 1)

    def printPath(self, begin):
        print("The Shortest Path Start from V" + str(begin))
        for i in range(self.vexnum):
            if self.dis[i].value == sys.maxsize:
                print("No Path form V" + str(begin) + " to V" + str(i + 1))
            else:
                print(self.dis[i].path, "=", self.dis[i].value)

    def searchPath(self, dest):
        return self.dis[dest - 1]
