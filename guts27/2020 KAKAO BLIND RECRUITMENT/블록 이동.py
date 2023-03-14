from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    visited = []
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    cost = 0
    p={(0,0),(0,1)}
    queue.append((p,cost))
    while queue:
        current, cost = queue.popleft()
        current = list(current)
        x,y = current[0][0],current[0][1]
        x2,y2 = current[1][0],current[1][1]
        if (x,y) == (n-1,n-1) or (x2,y2) == (n-1,n-1):
               return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0<=nx<n and 0<= ny < n and 0<=nx2<n and 0<= ny2 < n and board[nx][ny] != 1 and board[nx2][ny2] != 1:
                p = {(nx,ny),(nx2,ny2)}
                if p not in visited:
                    queue.append((p,cost+1))
                    visited.append(p)
        #수평
        # 현재 로봇이 가로로 놓여 있는 경우
        if x == x2:
            for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
                if board[x + i][y] == 0 and board[x2 + i][y2] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                    p={(x, y), (x + i, y)}
                    p2={(x2, y), (x2 + i, y)}
                    if p not in visited:
                        queue.append((p,cost+1))
                        visited.append(p)
                    if p2 not in visited:
                        queue.append((p2,cost+1))
                        visited.append(p2)
    # 현재 로봇이 세로로 놓여 있는 경우
        elif y == y2:
            for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
                if board[x][y + i] == 0 and board[x2][y2 + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                    p={(x, y), (x, y + i)}
                    p2={(x2, y2), (x2, y2 + i)}
                    if p not in visited:
                        queue.append((p,cost+1))
                        visited.append(p)
                    if p2 not in visited:
                        queue.append((p2,cost+1))
                        visited.append(p2)
            

