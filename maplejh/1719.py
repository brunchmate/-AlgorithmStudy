# https://www.acmicpc.net/problem/1753
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
# # 플로이드 와샬
# board = [[1e9] * n for _ in range(n)]
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     board[u - 1][v - 1] = w
#     board[v - 1][u - 1] = w
# ans = [[i + 1 for i in range(n)] for _ in range(n)]
# for i in range(n):
#     board[i][i] = 0
#     ans[i][i] = '-'
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] > board[i][k] + board[k][j]:
#                 board[i][j] = board[i][k] + board[k][j]
#                 ans[i][j] = ans[i][k]
# for a in ans:
#     print(*a)

# 다익스트라
board = defaultdict(list)
ans = [[i + 1 for i in range(n)] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    board[u - 1].append((v - 1, w))
    board[v - 1].append((u - 1, w))
for i in range(n):
    hq = []
    heapq.heappush(hq, (0, i))
    dist = [1e9] * n
    dist[i] = 0
    while hq:
        cost, k = heapq.heappop(hq)
        if dist[k] < cost:
            continue
        for j, c in board[k]:
            tmp = c + cost
            if dist[j] > tmp:
                dist[j] = tmp
                ans[j][i] = k + 1  # ??
                heapq.heappush(hq, (tmp, j))
for i in range(n):
    ans[i][i] = '-'
for a in ans:
    print(*a)
