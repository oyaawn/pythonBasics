def bfs(self,start):
    queue=[]
    visited={}
    visitedNodes=[]
    queue.append(start)
    visited[start]=True
    while queue:
        cur=queue.pop(0)
        visitedNodes.append(cur)
        for node in self.graph[cur]:
            if node not in visited:
                queue.append(node)
                visited[node]= True
    print(visitedNodes)
