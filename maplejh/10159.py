# https://www.acmicpc.net/problem/10159
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

# floyd-warshall
# n = int(input())
# m = int(input())
# board = [[1e9] * n for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     board[a - 1][b - 1] = 1
# for i in range(n):
#     board[i][i] = 1
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             board[i][j] = min(board[i][j], board[i][k] + board[k][j])
#
# ans = [0] * n
# for i in range(n):
#     for j in range(i + 1, n):
#         if board[i][j] == board[j][i] == 1e9:
#             ans[i] += 1
#             ans[j] += 1
# for a in ans:
#     print(a)

def dijkstra(start):
    dist1 = [1e9] * n
    dist1[start] = 0
    hq = [(0, start)]
    while hq:
        cost, x = heapq.heappop(hq)
        if dist1[x] < cost:
            continue
        for nx, nc in board[x]:
            tmp = nc + cost
            if dist1[nx] > tmp:
                heapq.heappush(hq, (tmp, nx))
                dist1[nx] = tmp
    return dist1


n = int(input())
m = int(input())
board = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1].append((b - 1, 1))
dist = []
for i in range(n):
    dist.append(dijkstra(i))
ans = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if dist[i][j] == dist[j][i] == 1e9:
            ans[i] += 1
            ans[j] += 1
for a in ans:
    print(a)

'''
board[i][j]=1: i>j 알고 있음
board[i][j]=inf: i>j 모름
a->b로 갈수 있으면 a>b 알 수 있음 
'''
