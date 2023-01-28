n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for j in range(n):
        for i in range(n):
            if i == k or j == k:
                    continue
            if graph[i][j] > graph[i][k]+[k][j]:
                print(-1)
            if graph[i][j] == graph[i][k] + graph[k][i]:
                graph[i][j] = 0
            
result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

if result == 0:
    print(-1)
else:
    print(result)
