from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,0,1,0],[0,1,0,-1]

def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    temp = 1
    visited[x][y] = cnt
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                temp +=1
                visited[nx][ny] = cnt
    return temp

visited = [[0]*m for _ in range(n)]
cnt = 1
tree = dict()
#그룹화
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            tree[cnt] = bfs(i,j,cnt)
            cnt = cnt + 1

#0인 애들만 체크 
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            size= []
            for z in range(4):
                nx,ny = i+dx[z], j+dy[z]
                if  0<=nx<n and 0<=ny<m and visited[nx][ny] != 0:
                    size.append(visited[nx][ny])
            result = 0
            for y in (set(size)):
                result += tree[y]
            answer = max(answer,result+1)

print(answer)
