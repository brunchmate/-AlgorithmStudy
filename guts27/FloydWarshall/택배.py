INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
graph2 = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            graph2[a][b] = '-'

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    graph2[a][b] = b
    graph2[b][a] = a


for k in range(1, n + 1):
    for a in range(1, n + 1): 
        for b in range(1, n + 1): 
            if graph[a][b] > (graph[a][k] + graph[k][b]):
                graph[a][b] = graph[a][k] + graph[k][b]
                graph2[a][b] = graph2[a][k]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph2[a][b], end=" ")
    print()
