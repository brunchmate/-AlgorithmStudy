from collections import deque

def dfs(v,visited,graph):
    index=1e9
    d_answer.append(v+1)
    if len(d_answer) == len(graph):
        return
    visited[v] = True
    for b in graph[v]:
        if visited[b] == False and index > b:
            index = b
    dfs(index,visited,graph)
    
def bfs(v,visited,graph):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        a = queue.popleft()
        b_answer.append(a+1)
        for b in graph[a]:
            if visited[b] == False:
                visited[b] = True
                queue.append(b)

global d_answer, b_answer
d_answer = []
b_answer = []
n,m,v = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [False for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(n):
    graph[i].sort()
dfs(v-1,visited,graph)
visited = [False for i in range(n)]
bfs(v-1,visited,graph)
print(*d_answer)
print(*b_answer)
