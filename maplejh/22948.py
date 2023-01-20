# https://www.acmicpc.net/problem/22948
import sys
from collections import deque
import heapq

input = sys.stdin.readline


def bfs(start, flag):
    q = deque()
    q.append(start)
    route[start][0 - flag] = start
    while q:
        x = q.popleft()
        nx = tree[x]
        route[x][1 - flag] = nx
        route[nx][0 - flag] = x
        if route[nx][1 - flag] != -1:
            break
        q.append(nx)


N = int(input())
circle = []
tree = [0] * (N + 1)
for _ in range(N):
    i, x, r = map(int, input().split())
    circle.append((x - r, i))
    circle.append((x + r, i))

# 괄호쌍 판별 <- 이 아이디어가 중요
heapq.heapify(circle)
stack = [0]
while circle:
    _, cur = heapq.heappop(circle)
    if stack[-1] == cur:
        stack.pop()
    else:
        tree[cur] = stack[-1]
        stack.append(cur)


A, B = map(int, input().split())
route = [[-1, -1] for _ in range(N + 1)]
bfs(A, 0)
bfs(B, 1)
answer = [str(A)]
s = A
while s != B:
    s = route[s][1]
    answer.append(str(s))
print(len(answer))
print(' '.join(answer))
