from collections import deque

N,M = map(int, input().split())

graph = [[] for _ in range(M+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

S,E = map(int,input().split())

for i in range(N):
    graph[i].sort()

def bfs(S,E):
    visited = [-1]*(N+1)
    visited[S] = 0
    queue = deque()
    queue.append((S,0))

    while queue:
        s, path = queue.popleft()
        if s == E:
            if path == 0:
              break
            else:
              return
        for i in graph[s]:
            if visited[i] == -1:
                visited[i] = s
                queue.append((i,path+1))
              
    visited = [-1]*(N+1)
    visited[E] = 0
    queue.append((E,0))
    while queue:
        e, path = queue.popleft()
        if e == S:
            break
        for i in graph[e]:
            if visited[i] == -1:
                visited[i] = e
                queue.append((i,path+1))
    return path

print(bfs(S,E))
