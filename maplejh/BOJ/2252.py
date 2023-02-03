# https://www.acmicpc.net/problem/2252
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
inode = [0] * (N + 1)
height = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    inode[B] += 1
    height[A].append(B)

q = deque()
ans = []
for i in range(1, N + 1):
    if not inode[i]:
        q.append(i)
        ans.append(i)

while q:
    x = q.popleft()
    for nx in height[x]:
        inode[nx] -= 1
        if not inode[nx]:
            ans.append(nx)
            q.append(nx)

print(*ans)
