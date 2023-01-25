import sys
input = sys.stdin.readline
import heapq

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
u,v = map(int,input().split())

def dijkstra(start):
    q = []
    distance = [1e9] * (n + 1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost 
                heapq.heappush(q,(cost,j[0]))
    return distance

origin = dijkstra(1)
v1 = dijkstra(u)
v2 = dijkstra(v)

result1 = origin[u]+v1[v]+v2[n]
result2 = origin[v]+v2[u]+v1[n]
result = min(result1,result2)
print(result if result < 1e9 else -1)
