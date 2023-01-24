import heapq
n,m,x = map (int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map (int,input().split())
    graph[a].append((b,c))
distance = [[1e9]*(n+1) for _ in range(n+1)]

def dijkstar(s,start):
    distance[s][start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[s][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[s][i[0]]:
                distance[s][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
     
for i in range(1,n+1):
    dijkstar(i,i)

student = 0
for i in range(1,n+1):
    if i == x:
        continue
    student = max(student,distance[i][x]+distance[x][i])

print(student)
