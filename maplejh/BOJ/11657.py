# https://www.acmicpc.net/problem/11657
import sys
from collections import defaultdict

input = sys.stdin.readline


def bellman_ford(start):
    dist[start] = 0
    for k in range(N):
        for i in board.keys():
            for j, c in board[i]:
                if dist[i] != 1e9 and dist[j] > dist[i] + c:
                    if k == N - 1:
                        return False
                    dist[j] = dist[i] + c
    return True


N, M = map(int, input().split())
board = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    board[A].append((B, C))
dist = [1e9] * (N + 1)
if bellman_ford(1):
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != 1e9 else -1)
else:
    print(-1)
