from collections import deque
k= int(input())
w,h = map (int,input().split())
graph = []
graph = [list(map(int, input().split())) for _ in range(h)]

dx,dy = [-1,0,1,0],[0,1,0,-1]
dx2, dy2 = [-2, -1, 1, 2, 2, 1, -1, -2],[1, 2, 2, 1, -1, -2, -2, -1]
visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
def bfs(x,y,k):
    queue = deque()
    queue.append((x,y,k))
    #벽
    while queue:
        x,y,k = queue.popleft()
        if x == h-1 and y== w-1:
            return visit[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visit[nx][ny][k] == 0:
                visit[nx][ny][k] = visit[x][y][k]+1
                queue.append((nx,ny,k))
        if k >0 :
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visit[nx][ny][k-1] == 0:
                    visit[nx][ny][k-1] = visit[x][y][k]+1
                    queue.append((nx,ny,k-1))
              
    return -1
        
print(bfs(0,0,k))
