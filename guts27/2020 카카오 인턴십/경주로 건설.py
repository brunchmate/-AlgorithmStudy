from collections import deque

def solution(board):
    queue = deque()
    queue.append([0,0,0,0])
    n = len(board)
    coner = 0
    direction = [[-1,0],[0,1],[1,0],[0,-1]]
    while queue:
        x,y,cx,cy = queue.popleft()

        for dx,dy in direction:
            nx = x+dx
            ny = y + dy
            if nx<0 or nx>=n or ny<0 or ny>= n or board[nx][ny] == 1:
                continue
            if (cx == 0 and cy == 0) or (cx == dx and cy == dy):
                if board[nx][ny] == 0 or board[nx][ny] >= board[x][y]+100:
                    board[nx][ny]= board[x][y]+100
                    queue.append((nx,ny,dx,dy))
                    
            else:
                if board[nx][ny] == 0 or board[nx][ny] >= board[x][y]+600:
                    board[nx][ny]= board[x][y]+600
                    queue.append((nx,ny,dx,dy))
    
    return board[n-1][n-1]
