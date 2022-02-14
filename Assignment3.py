import csv
import timeit

class Graph:
    def __init__(self):
        self.data = []
        self.size = 0
        pass

    def read(self, v):  # graph.read([])
        self.data = list(csv.reader(open(v)))
        self.size = len(self.data)

    def findMinimum(self, E):
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
        return val


    def process(self):
        T = [False] * self.size
        L = []  # edge [vertexIdA, vertexIdB, weight
        E = []

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j, self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findMinimum(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                T[targetEdge[1]] = True
                E = []
        print(L)
        length = 0
        for ele in L:
            length += int(ele[2])
        print("Minimum Spanning Tree Length is: ", length)

    def processOptimized(self):
        T = [False] * self.size
        L = []  # edge [vertexIdA, vertexIdB, weight
        E = []

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j, self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                target_edge = self.findMinimum(E)
                L.append(target_edge)
                E = []
        print(L)
        length = 0
        for ele in L:
            length += int(ele[2])
        print("Minimum Spanning Tree Length is: ", length)


g = Graph()
g.read("graph.csv")


print("MST non minheap ", timeit.Timer(g.process).timeit(number=1))
#print(timeit.Timer(g.processOptimized).timeit(number=1))
