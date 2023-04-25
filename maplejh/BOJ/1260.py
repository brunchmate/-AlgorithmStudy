# https://www.acmicpc.net/problem/1260
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dfs(depth, x):
    visited[x] = 1
    print(x, end=" ")
    if depth == N:
        return
    for nx in board[x]:
        if not visited[nx]:
            dfs(depth + 1, nx)


def bfs(sx):
    q = deque([sx])
    visited[sx] = 0
    while q:
        x=q.popleft()
        print(x,end=" ")
        for nx in board[x]:
            if visited[nx]:
                visited[nx]=0
                q.append(nx)


N, M, V = map(int, input().split())

board = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
for i in range(M + 1):
    board[i] = sorted(set(board[i]))
visited = [0] * (N + 1)
dfs(0, V)
print()
bfs(V)
