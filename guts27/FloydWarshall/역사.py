import sys # 개선
input = sys.stdin.readline # 개선

n,k  = map(int,input().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = True

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for _ in range(int(input())):
    a,b = map(int,input().split())
    if graph[a][b] == True:
        print(-1)
    elif graph[b][a] == True:
        print(1)
    else:
        print(0)
