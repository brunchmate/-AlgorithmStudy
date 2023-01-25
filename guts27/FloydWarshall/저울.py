
n = int(input())
m = int(input())
graph = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())  
  graph[a][b] = 1
  
for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
              
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] < 1e9:
            graph[j][i] = graph[i][j]
  
for i in range(1,n+1):
    print(graph[i].count(1e9)-1)
