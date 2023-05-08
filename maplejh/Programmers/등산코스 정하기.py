# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    def route(s):
        dist = [10e9] * (n + 1)
        dist[s] = 0
        q = [(0, s)]
        while q:
            cost, x = heapq.heappop(q)
            if x in gates:
                return cost
            if dist[x] < cost:
                continue
            for nx, nc in board[x]:
                if nx in summits:
                    continue
                if cost > nc:
                    nc = cost
                if dist[nx] > nc:
                    dist[nx] = nc
                    heapq.heappush(q, (nc, nx))
        return 10e9

    answer = [0, 10e9]
    board = defaultdict(list)
    summits = set(summits)
    gates = set(gates)
    for i, j, w in paths:
        board[i].append((j, w))
        board[j].append((i, w))
    for summit in sorted(summits):
        intensity = route(summit)
        if answer[-1] > intensity:
            answer = [summit, intensity]
    return answer
