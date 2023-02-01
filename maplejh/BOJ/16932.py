# https://www.acmicpc.net/problem/16932
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(sx, sy, gn):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = gn
    groups[gn] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = gn
                    q.append((nx, ny))
                    groups[gn] += 1


answer = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 그룹의 사이즈 미리 계산/저장
groups = dict()
groups[0] = 0
visited = [[0] * M for _ in range(N)]
idx = 1
for i in range(N):
    for j in range(M):
        if board[i][j] and not visited[i][j]:
            bfs(i, j, idx)
            idx += 1
# 0인 부분에 상하좌우 모양 계산
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            shape = set()
            for di, dj in d:
                ni = i + di
                nj = j + dj
                if -1 < ni < N and -1 < nj < M:
                    shape.add(visited[ni][nj])
            answer = max(sum([groups[k] for k in shape]) + 1, answer)
print(answer)
