# https://www.acmicpc.net/problem/20058
import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


def rotate90(sx, sy, ss):
    for x in range(ss):
        for y in range(ss):
            tmp[y][ss - x - 1] = board[sx + x][sy + y]
    for x in range(ss):
        for y in range(ss):
            board[sx + x][sy + y] = tmp[x][y]


def bfs(sx, sy):
    global total
    q = deque([(sx, sy)])
    res = 1
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            if -1 < nx < k and -1 < ny < k:
                if board[nx][ny] and not visited[nx][ny]:
                    total += board[nx][ny]
                    res += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return res


n, _ = map(int, input().split())
k = 2 ** n
board = [list(map(int, input().split())) for _ in range(k)]
magic = list(map(int, input().split()))

for l in magic:
    tmp = [[0] * 2**l for _ in range(2**l)]
    if l:
        for i in range(0, k, 2 ** l):
            for j in range(0, k, 2 ** l):
                rotate90(i, j, 2 ** l)
    minus = []
    for i in range(k):
        for j in range(k):
            if board[i][j]:
                cnt = 0
                for di in range(4):
                    ni = i + dx[di]
                    nj = j + dy[di]
                    if -1 < ni < k and -1 < nj < k:
                        if board[ni][nj]:
                            cnt += 1
                if cnt < 3:
                    minus.append((i, j))
    for mi, mj in minus:
        board[mi][mj] -= 1

total = 0
group = 0
visited = [[0] * k for _ in range(k)]
for i in range(k):
    for j in range(k):
        if board[i][j] and not visited[i][j]:
            total += board[i][j]
            group = max(group, bfs(i, j))
print(total)
print(group)
