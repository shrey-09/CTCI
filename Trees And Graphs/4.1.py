# 4.1
# Is there a path between two nodes of a graph.

visited=[False for x in range(100)]

def isThereAPath(adj,src,des):
    if src==des:
        return True
    if visited[src]:
        return False
    else:
        visited[src]=True
        for x in range(len(adj[src])):
            if isThereAPath(adj,adj[src][x],des):
                return True
        return False


adj=[[1],
    [1,3],
    [3,4],
    [4],
    [2,4,3]]
print(isThereAPath(adj,0,2))
    