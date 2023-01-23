# https://www.acmicpc.net/problem/1719
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
board = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    board[u].append((v, w))

dist = [1e9] * (V + 1)
hq = []
heapq.heappush(hq, (0, K))
dist[K] = 0
while hq:
    cost, i = heapq.heappop(hq)
    if dist[i] < cost:
        continue
    for j, c in board[i]:
        tmp = cost + c
        if dist[j] > tmp:
            dist[j] = tmp
            heapq.heappush(hq, (tmp, j))

for idx in range(1, V + 1):
    print(dist[idx] if dist[idx] != 1e9 else "INF")
