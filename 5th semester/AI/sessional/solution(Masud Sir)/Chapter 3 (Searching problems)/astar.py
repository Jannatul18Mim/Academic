import heapq

def astar(graph,start,goal,h):
    openq=[]
    heapq.heappush(openq,(h(start),0,start))
    parent={start:None}
    g={start:0}
    closed=set()
    while openq:
        f,gv,u=heapq.heappop(openq)
        if u in closed:
            continue
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path))
        closed.add(u)
        for v,w in graph.get(u,{}).items():
            ng=g[u]+w
            if v not in g or ng<g[v]:
                g[v]=ng
                parent[v]=u
                heapq.heappush(openq,(ng+h(v),ng,v))
    return []

if __name__=="__main__":
    graph={
        'A':{'B':1,'C':4},
        'B':{'C':2,'D':5},
        'C':{'D':1},
        'D':{}
    }
    h=lambda x:{'A':7,'B':6,'C':2,'D':0}[x]
    print(astar(graph,'A','D',h))