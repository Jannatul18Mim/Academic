import heapq

def greedy_best_first(graph,start,goal,h):
    pq=[]
    heapq.heappush(pq,(h(start),start))
    visited=set()
    parent={start:None}
    while pq:
        _,u=heapq.heappop(pq)
        if u in visited:
            continue
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path))
        visited.add(u)
        for v in graph.get(u,[]):
            if v not in visited:
                parent[v]=u
                heapq.heappush(pq,(h(v),v))
    return []

if __name__=="__main__":
    g={'A':['B','C'],'B':['D'],'C':['D'],'D':[]}
    h=lambda x:{'A':3,'B':2,'C':1,'D':0}[x]
    print(greedy_best_first(g,'A','D',h))