def dls(graph,start,goal,limit):
    stack=[(start,0)]
    parent={start:None}
    visited=set([start])
    while stack:
        u,d=stack.pop()
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path))
        if d<limit:
            for v in reversed(graph.get(u,[])):
                if (v,d+1) not in visited:
                    visited.add(v)
                    parent[v]=u
                    stack.append((v,d+1))
    return []

if __name__=="__main__":
    g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
    print(dls(g,'A','E',2))