# https://www.acmicpc.net/problem/23289
import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check():
    for ox, oy in office:
        if board[ox][oy] < k:
            return False
    return True


def spread():
    dd = {2: [(3,), (0, 3), (2, 3)],
          3: [(0,), (3, 0), (1, 0)],
          1: [(1,), (0, 1), (2, 1)],
          4: [(2,), (1, 2), (3, 2)]
          }
    for ax, ay, ad in ac:
        visited = [[0] * m for _ in range(n)]
        cur = dd[ad]
        ax += d[cur[0][0]][0]
        ay += d[cur[0][0]][1]
        visited[ax][ay] = 5
        board[ax][ay] += 5
        q = deque()
        q.append((ax, ay))
        while q:
            x, y = q.popleft()
            if visited[x][y] == 1:
                continue
            for route in cur:
                nx = x
                ny = y
                for di in route:
                    if wall[nx][ny][di]:
                        break
                    nx += d[di][0]
                    ny += d[di][1]
                    if not (-1 < nx < n and -1 < ny < m):
                        break
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] - 1
                        board[nx][ny] += visited[nx][ny]
                        q.append((nx, ny))


def mix():
    tmp = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for di in range(4):
                if wall[x][y][di]:
                    continue
                nx = d[di][0] + x
                ny = d[di][1] + y
                if -1 < nx < n and -1 < ny < m:
                    diff = abs(board[nx][ny] - board[x][y]) // 4
                    if not diff: continue
                    if board[nx][ny] > board[x][y]:
                        tmp[x][y] += diff
                    elif board[nx][ny] < board[x][y]:
                        tmp[x][y] -= diff
    for x in range(n):
        for y in range(m):
            board[x][y] += tmp[x][y]


def decrease():
    for x in range(n):
        if board[x][0]:
            board[x][0] -= 1
        if board[x][-1]:
            board[x][-1] -= 1
    for y in range(1, m - 1):
        if board[0][y]:
            board[0][y] -= 1
        if board[-1][y]:
            board[-1][y] -= 1


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wall = [[[0, 0, 0, 0] for _ in range(m)] for _ in range(n)]  # 벽의 위치
for _ in range(int(input())):
    xx, yy, ss = map(int, input().split())
    if ss == 0:
        wall[xx - 1][yy - 1][0] = 1
        wall[xx - 2][yy - 1][2] = 1
    else:
        wall[xx - 1][yy - 1][1] = 1
        wall[xx - 1][yy][3] = 1
ac = []
office = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 5:
            office.append((i, j))
            board[i][j] = 0
        elif board[i][j] >= 1:
            ac.append((i, j, board[i][j]))
            board[i][j] = 0
for t in range(102):
    if check():
        break
    spread()
    mix()
    decrease()
print(t)
