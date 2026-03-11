import heapq

def ucs(graph,start,goal):
    pq=[]
    heapq.heappush(pq,(0,start))
    g={start:0}
    parent={start:None}
    visited=set()
    while pq:
        cost,u=heapq.heappop(pq)
        if u in visited:
            continue
        if u==goal:
            path=[]
            while u is not None:
                path.append(u)
                u=parent[u]
            return list(reversed(path)),cost
        visited.add(u)
        for v,w in graph.get(u,{}).items():
            ng=g[u]+w
            if v not in g or ng<g[v]:
                g[v]=ng
                parent[v]=u
                heapq.heappush(pq,(ng,v))
    return [],float('inf')

if __name__=="__main__":
    g={'A':{'B':1,'C':4},'B':{'C':2,'D':5},'C':{'D':1},'D':{}}
    print(ucs(g,'A','D'))