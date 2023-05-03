import sys
input = sys.stdin.readline
n,m =map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1](이건 자기 자신)

for _ in range(m):
    x,y,x2,y2 = map(int,input().split())
    sum = dp[x2][y2] - dp[x-1][y2] - dp[x2][y-1]+dp[x-1][y-1]
        
    print(sum)
