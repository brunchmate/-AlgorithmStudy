# ttps://www.acmicpc.net/problem/1504
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline


def dijkstra(start):
    dist = [1e9] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, x = heapq.heappop(hq)
        if dist[x] < cost:
            continue
        for nx, nc in board[x]:
            tmp = cost + nc
            if dist[nx] > tmp:
                heapq.heappush(hq, (tmp, nx))
                dist[nx] = tmp
    return dist


n, e = map(int, input().split())
board = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))
v1, v2 = map(int, input().split())
dist1 = dijkstra(v1)
dist2 = dijkstra(v2)
answer = min(dist1[1] + dist1[v2] + dist2[n], dist2[1] + dist2[v1] + dist1[n], 1e9)
if answer == 1e9:
    print(-1)
else:
    print(answer)
