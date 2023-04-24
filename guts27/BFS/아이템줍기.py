from collections import deque
def bfs(x,y,ix,iy,graph):
    queue = deque()
    queue.append((x*2,y*2))
    dx,dy = [0,-1,0,1],[-1,0,1,0]
    visited = [[1] * 102 for i in range(102)] 
    visited[x*2][y*2] = 0
    
    while queue:
        x,y = queue.popleft()
        if x == ix * 2 and y == iy * 2:
            return visited[ix*2][iy*2]//2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

        
def fill(x,y, x2,y2,graph):
    for i in range(x*2,x2*2+1):
        for j in range(y*2,y2*2+1):
            if x*2 < i < x2*2 and y*2 < j < y2*2:
                 graph[i][j] = 0
            elif graph[i][j] != 0:
                graph[i][j] = 1
    

    return graph
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    #1. 사각형 채우기
    #2. BFS
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    
    for x,y, x2,y2 in rectangle:
        graph = fill(x,y, x2,y2,graph)

    answer = bfs(characterX, characterY, itemX, itemY,graph)

    return answer
