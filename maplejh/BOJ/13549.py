# https://www.acmicpc.net/problem/13549
# 0-1 bfs
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# visited = [10001] * 100001
# q = deque([n])
# visited[n] = 0
# while q:
#     x = q.popleft()
#     if -1 < x + x < 100001 and visited[x + x] > visited[x]:
#         visited[x + x] = visited[x]
#         q.appendleft(x + x)
#     if -1 < x + 1 < 100001 and visited[x + 1] > visited[x] + 1:
#         visited[x + 1] = visited[x] + 1
#         q.append(x + 1)
#     if -1 < x - 1 < 100001 and visited[x - 1] > visited[x] + 1:
#         visited[x - 1] = visited[x] + 1
#         q.append(x - 1)
# print(visited[k])


import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
q = [(0, n)]
visited = [0] * 100001
while q:
    cost, x = heapq.heappop(q)
    if x < 0 or x > 100000:
        continue
    if visited[x]:
        continue
    if x == k:
        print(cost)
        break
    visited[x] = 1
    heapq.heappush(q, (cost + 1, x - 1))
    if x < k:
        if 0 < x:
            heapq.heappush(q, (cost, x * 2))
        heapq.heappush(q, (cost + 1, x + 1))
