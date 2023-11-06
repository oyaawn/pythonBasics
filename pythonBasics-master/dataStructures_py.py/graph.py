class Graph:
    def __init__(self, node1, node2):
        self.graph={}

    def addNode(self,node):
        self.graph[node]={}

    def addEdgeNoWeight(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1]=[node2]
        else:
            self.graph[node1].append(node2)

        if node2 not in self.graph:
            self.graph[node2]=[node1]
        else:
            self.graph[node2].append(node1)

    def addEdgeWeight(self,node1,node2,weight):
        if node1 not in self.graph:
            self.graph[node1]={node2:weight}
        else:
            self.graph[node1][node2]=weight

        if node2 not in self.graph:
            self.graph[node2]={node1:weight}
        else:
            self.graph[node2][node1]=weight

    def printGraph(self):
        for node in self.graph:
            print(node, ":", self.graph[node])

g=Graph()
g.addEdgeWeight('A', 'B', 1)
g.addEdgeWeight('A', 'C', 2)
g.printGraph()

