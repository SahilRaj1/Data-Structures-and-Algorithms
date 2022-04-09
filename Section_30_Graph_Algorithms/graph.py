""" Creating a Graph"""

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    # Breadth First Search
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue != []:
            curVertex = queue.pop(0)
            print(curVertex, end=" ")
            for adjVertex in self.gdict[curVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)

    # Depth First Search
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack != []:
            curVertex = stack.pop()
            print(curVertex, end=" ")
            for adjVertex in self.gdict[curVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    stack.append(adjVertex)



dict = {
    1 : [2, 3],
    2 : [1, 4, 5],
    3 : [1, 5],
    4 : [2, 5, 6],
    5 : [4, 6],
    6 : [4, 5]
}

graph = Graph(dict)
graph.addEdge(5, 3)

graph.bfs(1)
print()

graph.dfs(1)
print()


                
                

