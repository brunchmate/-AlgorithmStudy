n = int(input())

graph = list(map(int,input().split()))
graph1 = [[] for _ in range(n)]
graph1[0]=graph[0]
for i in range(1,n):
    if graph[i] > graph1[i-1] + graph[i]:
        graph1[i]=graph[i]
    else:
        graph1[i]=graph1[i-1] + graph[i]
print(max(graph1))
