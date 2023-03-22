from collections import deque
from itertools import permutations
def bfs(board,x,y,tx,ty):
    queue = deque()
    queue.append((x,y))
    visited = [[1e9 for _ in range(4)] for _ in range(4)]
    visited[x][y] = 0
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        if x == tx and y == ty:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4 and board[nx][ny] == 0:
                nx, ny = nx + dx[i], ny + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
def solution(board, r, c):
    answer = 1e9
    card = []
    cgraph = [[] for _ in range(7)]

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cgraph[board[i][j]].append((i,j))
                if board[i][j] not in card:
                    card.append(board[i][j])
    
    for perm in permutations(card,len(card)):
        score = 0
        for p in perm:
            x,y = cgraph[p][0]
            x2,y2 = cgraph[p][1]
            temp = bfs(board,r,c,x,y)+bfs(board,x,y,x2,y2)
            temp2 = bfs(board,r,c,x2,y2)+bfs(board,x2,y2,x,y)
            if temp <temp2:
                r,c = x2,y2
                score += temp
            else:
                r,c = x,y
                score += temp2
        answer = min(answer,score)
    return answer
