# https://www.acmicpc.net/problem/1600
import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    q = deque()
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    q.append((0, 0, 0))  # 말, x,y
    while q:
        horse, x, y = q.popleft()
        if x == H - 1 and y == W - 1:
            return visited[x][y][horse]
        for dx, dy in d:
            # 인접한 곳으로 이동
            nx = x + dx
            ny = y + dy
            if -1 < nx < H and -1 < ny < W:
                if not board[nx][ny] and not visited[nx][ny][horse]:
                    visited[nx][ny][horse] = visited[x][y][horse] + 1
                    q.append((horse, nx, ny))
            # 말처럼 움직임
            if horse >= K:
                continue
            for i in [-1, 1]:
                hx = nx + dx + dy * i
                hy = ny + dx * i + dy
                if -1 < hx < H and -1 < hy < W:
                    if not board[hx][hy] and not visited[hx][hy][horse + 1]:
                        visited[hx][hy][horse + 1] = visited[x][y][horse] + 1
                        q.append((horse + 1, hx, hy))
    return -1


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
print(bfs())
