# https://www.acmicpc.net/problem/1238
import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(start, board):
    hq = []
    dist = [1e9] * (N + 1)
    hq.append((0, start))
    dist[start] = 0
    while hq:
        cost, cur = heapq.heappop(hq)
        if dist[cur] < cost:
            continue
        for j, c in board[cur]:
            tmp = c + cost
            if tmp < dist[j]:
                heapq.heappush(hq, (tmp, j))
                dist[j] = tmp
    return dist


N, M, X = map(int, input().split())
board1 = defaultdict(list)
board2 = defaultdict(list)
for _ in range(M):
    s, e, t = map(int, input().split())
    board1[s].append((e, t))
    board2[e].append((s, t))

go = dijkstra(X, board1)
come = dijkstra(X, board2)
print(max([go[i] + come[i] for i in range(1, N + 1)]))
