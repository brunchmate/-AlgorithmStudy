# https://school.programmers.co.kr/learn/courses/30/lessons/72413
from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    def dijkstra(start):
        dist = [2e9] * n
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            cur, x = heapq.heappop(hq)
            if dist[x] < cur:
                continue
            for nx, nc in board[x]:
                tmp = nc + cur
                if dist[nx] > tmp:
                    dist[nx] = tmp
                    heapq.heappush(hq, (tmp, nx))
        return dist

    board = defaultdict(list)
    for c, d, f in fares:
        board[c - 1].append((d - 1, f))
        board[d - 1].append((c - 1, f))
    cost = [dijkstra(i) for i in [s - 1, a - 1, b - 1]]
    answer = cost[0][a - 1] + cost[0][b - 1]
    for k in range(n):
        if answer > cost[0][k] + cost[1][k] + cost[2][k]:
            answer = cost[0][k] + cost[1][k] + cost[2][k]
    return answer
