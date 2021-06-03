# 8.2
# Robot In A Grid

def robotInAGrid(grid):
    #initialization
    n,m=len(grid),len(grid[0])
    dp=[[0 for x in range(m+1)] for y in range(n+1)]
    if grid[0][0]==1:
        dp[0][0]=0
    else:
        dp[0][0]=1
    for x in range(1,m+1):
        if dp[0][x-1]==0:
            dp[0][x]=0
        elif grid[0][x]==1:
            dp[0][x]=0
        else:
            dp[0][x]=dp[0][x-1]
    for x in range(1,n+1):
        if dp[x-1][0]==0:
            dp[x][0]=0
        elif grid[x][0]==0:
            dp[x][0]=0
        else:
            dp[x][0]=dp[x-1][0]
    #dp approach
    for x in range(1,n+1):
        for y in range(1,m+1):
            if grid[x-1][y-1]==1:
                dp[x][y]=0
            else:
                dp[x][y]=dp[x][y-1]+dp[x-1][y]
    return dp[n][m]