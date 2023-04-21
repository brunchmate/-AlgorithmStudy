from collections import deque

def dfs(a):
    print(a, end = " ")
    visited[a] = True
    for b in graph[a]:
        if visited[b] == False:
            dfs(b)
    
def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = True
    while queue:
        a = queue.popleft()
        print(a, end= " ")
        for b in graph[a]:
            if visited[b] == False:
                visited[b] = True
                queue.append(b)
                
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
#내가 틀린 이유!!!!!!!
#for i in range(n):
#    graph[i].sort()
# 정렬
for i in graph:
    i.sort()
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)
