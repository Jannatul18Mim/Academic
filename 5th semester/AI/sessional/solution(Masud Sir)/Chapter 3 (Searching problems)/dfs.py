def dfs(graph,start,goal):
    stack=[start]
    visited=set([start])
    parent={start:None}
    while stack:
        u=stack.pop()
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path))
        for v in reversed(graph.get(u,[])):
            if v not in visited:
                visited.add(v)
                parent[v]=u
                stack.append(v)
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
    print(dfs(graph,'A','F'))