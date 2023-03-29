# https://www.acmicpc.net/problem/16234
from collections import deque

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(sx, sy):
    union = set()
    p = board[sx][sy]
    q = deque()
    q.append((sx, sy))
    union.add((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if not visited[nx][ny]:
                    if l <= abs(board[nx][ny] - board[x][y]) <= r:
                        visited[nx][ny] = 1
                        p += board[nx][ny]
                        q.append((nx, ny))
                        union.add((nx, ny))
    if len(union) == 1:
        return False
    p = p // len(union)
    for ux, uy in union:
        board[ux][uy] = p
    return True


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for t in range(2001):
    moved = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i % 2, n, 2):
            if not visited[i][j]:
                moved |= bfs(i, j)
    if not moved:
        print(t)
        break
