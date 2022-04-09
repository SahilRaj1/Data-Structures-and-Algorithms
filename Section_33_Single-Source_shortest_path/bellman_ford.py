class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def printSolution(self, dist):
        print("Vertex distance from source")
        for k, v in dist.items():
            print(f" {k} : {v}")

    def bellmanFord(self, src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for i in range(self.v -1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("The graph contains a negative cycle")
                return
        
        self.printSolution(dist)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)
g.bellmanFord("E")

