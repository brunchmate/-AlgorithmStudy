# https://www.acmicpc.net/problem/22868
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(start, end):
    q = deque()
    visited = defaultdict(int)
    q.append(start)
    visited[start] = start
    while q:
        x = q.popleft()
        if x == end:
            break
        for nx in board[x]:
            if not visited[nx] and nx not in route:
                visited[nx] = x
                q.append(nx)
    k, v = end, visited[end]
    while k != v:
        route.add(k)
        k, v = v, visited[v]


N, M = map(int, input().split())
board = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    board[A].append(B)
    board[B].append(A)
for key in board.keys():
    board[key].sort()
S, E = map(int, input().split())
route = set()
bfs(S, E)
bfs(E, S)
print(len(route))
