from collections import deque
##list() 함수에 문자열을 넣으면 한 문자씩 다 나누어 리스트를 생성합니다. (공백도 한 문자로 취급)
graph = [list(input()) for _ in range(8)]

def bfs(x,y):
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1,0], [-1, 0, 1, -1, 1, -1, 0, 1,0]
    queue = deque()
    queue.append((x,y))
    count = 0
    visited = [[False]*8 for _ in range(8)] 
    while queue:
        count = len(queue)
        for _ in range(count):
            x, y = queue.popleft()
            if visited[x][y] == False:
                for i in range(9):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >=8 or ny<0 or ny>=8 or graph[nx][ny] == '#':
                        continue
                    if nx == 0:
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
                    elif graph[nx-1][ny] != '#':
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
                    if nx == x and ny == y and graph[nx-1][ny] != '#':
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
                        visited[x][y] = True
            else:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >=8 or ny<0 or ny>=8 or graph[nx][ny] == '#' or graph[nx][ny] == 1:
                        continue
                    if nx == 0:
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
                    elif graph[nx-1][ny] != '#':
                        graph[nx][ny] = 1
                        queue.append((nx,ny))

        for i in range(7,-1,-1):
            for j in range(8):
                if graph[i][j] == '#':
                    if i == 7:
                        graph[i][j] = '.'
                    else:
                        graph[i][j] = '.'
                        graph[i+1][j] = '#'
   
  
    return graph[0][7]
result = bfs(7,0)
if result == 1:
    print(1)
else:
    print(0)
