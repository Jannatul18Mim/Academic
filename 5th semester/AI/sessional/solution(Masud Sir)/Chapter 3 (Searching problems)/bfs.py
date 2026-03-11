import collections

def bfs(graph, start, goal):
    q=collections.deque([start])
    visited={start}
    parent={start:None}
    while q:
        u=q.popleft()
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path))
        for v in graph.get(u,[]):
            if v not in visited:
                visited.add(v)
                parent[v]=u
                q.append(v)
    return []

if __name__=="__main__":
    graph={
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]
    }
    print(bfs(graph,'A','F'))