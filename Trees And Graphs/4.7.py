# 4.7
# Build Order (Topological Sort)

def buildOrder(adj,n):
    visited=[False for x in range(n)]
    stack=[]
    
    def dfs(src):
        if visited[src]:
            return
        visited[src]=True
        for x in range(len(adj[src])):
            if not visited[adj[src][x]]:
                dfs(adj[src][x])
        stack.append(src)
        return

    for x in range(n):
        if not visited[x]:
            dfs(x)
    return stack[::-1]

def create_adj(lis,n):
    adj=[[] for x in range(n)]
    for x in range(len(lis)):
        a,b=lis[x]  #b depends on a
        adj[a].append(b)
    return adj

n=7
# this is the example given, in the solution
adj=[
    [4],
    [0,4],
    [0],
    [6],
    [],
    [1,0,2],
    []]
print(buildOrder(adj,n))