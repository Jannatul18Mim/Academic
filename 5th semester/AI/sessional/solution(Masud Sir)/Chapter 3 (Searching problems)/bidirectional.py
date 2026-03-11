import collections

def bidirectional_bfs(graph, start, goal):
    if start==goal:
        return [start]
    q1=collections.deque([start])
    q2=collections.deque([goal])
    p1={start:None}
    p2={goal:None}
    v1={start}
    v2={goal}
    meet=None
    while q1 and q2:
        u=q1.popleft()
        for x in graph.get(u,[]):
            if x not in v1:
                v1.add(x)
                p1[x]=u
                q1.append(x)
                if x in v2:
                    meet=x
                    q2.clear()
                    break
        if meet:
            break
        v=q2.popleft()
        for y in graph.get(v,[]):
            if y not in v2:
                v2.add(y)
                p2[y]=v
                q2.append(y)
                if y in v1:
                    meet=y
                    q1.clear()
                    break
        if meet:
            break
    if not meet:
        return []
    left=[]
    x=meet
    while x is not None:
        left.append(x)
        x=p1[x]
    left=list(reversed(left))
    right=[]
    y=p2[meet]
    while y is not None:
        right.append(y)
        y=p2[y]
    return left+right

if __name__=="__main__":
    g={'A':['B'], 'B':['C'], 'C':['D'], 'D':['E'], 'E':[]}
    print(bidirectional_bfs(g,'A','E'))