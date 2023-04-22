from collections import deque
def bfs(x,y):
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
            #이거 필요없음 BFS 니깐, 가까운 노드부터 우선 탐색
            if graph[nx][ny] > 1 and graph[nx][ny] > graph[x][y]+1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
bfs(0,0)
print(graph[n-1][m-1])
