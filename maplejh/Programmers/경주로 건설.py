# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque


# bfs
def solution(board):
    n = len(board)
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[[1e9, 1e9, 1e9, 1e9] for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))
    q.append((0, 0, 2))
    visited[0][0] = [0, 0, 0, 0]
    while q:
        x, y, dd = q.popleft()
        for ndd in range(4):
            nx = x + d[ndd][0]
            ny = y + d[ndd][1]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny]:
                    continue
                cost = 100
                if (dd + ndd) % 2:
                    cost += 500
                if visited[x][y][dd] + cost < visited[nx][ny][ndd]:
                    visited[nx][ny][ndd] = visited[x][y][dd] + cost
                    q.append((nx, ny, ndd))
    return min(visited[-1][-1])
