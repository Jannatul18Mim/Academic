from dfs_limited import dls

def iddfs(graph,start,goal,max_depth):
    for l in range(max_depth+1):
        p=dls(graph,start,goal,l)
        if p:
            return p
    return []

if __name__=="__main__":
    g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
    print(iddfs(g,'A','E',3))