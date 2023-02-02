# https://www.acmicpc.net/problem/14567
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
inode = [0] * N
board = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    board[A - 1].append(B - 1)
    inode[B - 1] += 1

q = deque()
ans = [0] * N
for i in range(N):
    if not inode[i]:
        q.append(i)
        ans[i] = 1
while q:
    x = q.popleft()
    for nx in board[x]:
        inode[nx] -= 1
        if not inode[nx]:
            q.append(nx)
            ans[nx] = ans[x] + 1
print(*ans)
