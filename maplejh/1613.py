# https://www.acmicpc.net/problem/1613
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


# # floyd-warshall 은 pypy로 해야 통과 시간복잡도 O(n**3)
# inf = 1e9
# n, k = map(int, input().split())
# board = [[inf] * n for _ in range(n)]
# for _ in range(k):
#     a, b = map(int, input().split())
#     board[a - 1][b - 1] = 1
# for h in range(n):
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] > board[i][h] + board[h][j]:
#                 board[i][j] = board[i][h] + board[h][j]
# s = int(input())
# for _ in range(s):
#     a, b = map(int, input().split())
#     if board[a - 1][b - 1] != inf:
#         print(-1)
#     elif board[b - 1][a - 1] != inf:
#         print(1)
#     else:
#         print(0)

# 다익스트라 python3로 통과 시간복잡도 O(n*k*logn)
def dijkstra(start):
    dist = [1e9] * (n + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, x = heapq.heappop(q)
        if dist[x] < cost:
            continue
        for nx, nc in board[x]:
            tmp = nc + cost
            if dist[nx] > tmp:
                dist[nx] = tmp
                heapq.heappush(q, (tmp, nx))
    return dist


n, k = map(int, input().split())
board = defaultdict(list)
for _ in range(k):
    a, b = map(int, input().split())
    board[a].append((b, 1))

arr = [[]]
for i in range(1, n + 1):
    arr.append(dijkstra(i))

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if arr[a][b] != 1e9:
        print(-1)
    elif arr[b][a] != 1e9:
        print(1)
    else:
        print(0)
