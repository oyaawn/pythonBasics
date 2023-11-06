class Graph:
    def __init__(self):
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


    def bfs(self,start):
        visited={}
        queue=[]
        queue.append(start)
        visited[start]=True
        visitedNodes = []
        while queue:
            cur=queue.pop(0)
            visitedNodes.append(cur)
            for node in self.graph[cur]:
                if node not in visited:
                    queue.append(node)
                    visited[node]=True
        return visitedNodes

    def dfs(self,start):
        visited={}
        stack=[]
        stack.append(start)
        visited[start]=True
        visitedNodes=[]
        while stack:
            cur=stack.pop()
            visitedNodes.append(cur)
            for node in self.graph[cur]:
                if node not in visited:
                    stack.append(node)
                    visited[node]=True
        return visitedNodes

    def printMenu(self):
        print("Please select a traversal method:")
        print("1. BFS")
        print("2. DFS")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            start = input("Enter the starting node: ")
            print("BFS traversal:", self.bfs(start))
        elif choice == "2":
            start = input("Enter the starting node: ")
            print("DFS traversal:", self.dfs(start))
        else:
            print("Invalid choice")

g=Graph()
g.addEdgeWeight('A', 'B', 1)
g.addEdgeWeight('A', 'C', 2)
g.printGraph()
g.printMenu()

