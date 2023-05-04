# https://www.acmicpc.net/problem/1987
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

answer = 0
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
q = deque([(0, 0, board[0][0])])
visited = [[set() for _ in range(c)] for _ in range(r)]
while q:
    x, y, route = q.popleft()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if -1 < nx < r and -1 < ny < c:
            if board[nx][ny] in route:
                continue
            cur = ''.join(sorted(route + board[nx][ny]))
            if cur not in visited[nx][ny]:
                q.append((nx, ny, cur))
                visited[nx][ny].add(cur)
print(len(route))
