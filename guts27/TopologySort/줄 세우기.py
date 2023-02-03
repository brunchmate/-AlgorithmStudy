from collections import deque
n,m = map(int, input().split())
indegree = [0]*(n+1)
graph= [[] for _ in range(n+1)]
result= []

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
  
def topology_sort():
    q = deque()
    for i in range(1,n+1):
        if indegree[i] ==0:
            q.append((i,1))

    while q:
        now, cnt = q.popleft()
        result.append((now,cnt))
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i,cnt+1))

topology_sort()
result.sort(key = lambda x:x[1])
for r in result:
    print(r[0],end = ' ')
