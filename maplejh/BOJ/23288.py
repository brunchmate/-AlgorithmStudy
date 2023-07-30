# https://www.acmicpc.net/problem/23288
import sys
from collections import deque

input = sys.stdin.readline


def bfs(si, sj):
    q = deque()
    cur = board[si][sj]
    visited = set()
    visited.add((si, sj))
    q.append((si, sj))
    res = 1
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = di + i
            nj = dj + j
            if -1 < ni < n and -1 < nj < m:
                if board[ni][nj] == cur and (ni, nj) not in visited:
                    q.append((ni, nj))
                    visited.add((ni, nj))
                    res += 1
    return res * cur


def locate():
    if dd == 0:
        tmp = dice[2]
        dice[2] = 7 - dice[0]
        dice[0] = tmp
    elif dd == 1:
        tmp = dice[1]
        dice[1] = 7 - dice[0]
        dice[0] = tmp
    elif dd == 2:
        tmp = dice[0]
        dice[0] = 7 - dice[2]
        dice[2] = tmp
    elif dd == 3:
        tmp = dice[0]
        dice[0] = 7 - dice[1]
        dice[1] = tmp


n, m,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [6, 5, 3]  # 아래, 앞, 오른쪽

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dd = 0
dx = 0
dy = 0
answer = 0
for _ in range(k):
    nx = d[dd][0] + dx
    ny = d[dd][1] + dy
    if not (-1 < nx < n and -1 < ny < m):
        dd = (dd + 2) % 4
        nx = d[dd][0] + dx
        ny = d[dd][1] + dy
    dx = nx
    dy = ny
    answer += bfs(dx, dy)
    locate()  # 주사위 방향조정
    if dice[0] > board[dx][dy]:
        dd = (dd + 1) % 4
    elif dice[0] < board[dx][dy]:
        dd = (dd - 1) % 4

print(answer)
