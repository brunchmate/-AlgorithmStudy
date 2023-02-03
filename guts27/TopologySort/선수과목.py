from collections import deque

n,m = map(int, input().split())
indegree = [0] * (n+1)
result = [0]*(n+1)
z = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append((i,1))

    while q:
        now, cnt = q.popleft()
        result[now] = cnt
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i,cnt+1))

topology_sort()
# 이거를 바꿀 필요는 없어 보임 감이, 
print(*result[1:])
