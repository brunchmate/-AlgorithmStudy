from collections import deque

def bfs(arr):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque(arr)
    result = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny <0 or ny >= n or graph[nx][ny] != 0:
                continue
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))

n,m  =map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
arr = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            arr.append([i,j])
bfs(arr)
flag = False
flag=[True for i in range(m) for j in range(n) if graph[i][j]==0]
if flag:
    print(-1)
else:
    print(max(map(max,graph))-1)
