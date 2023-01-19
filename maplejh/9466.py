# https://www.acmicpc.net/problem/9466
import sys
from collections import deque

input = sys.stdin.readline


def cycle(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    end = start
    while q:
        x = q.popleft()
        nx = board[x]
        if visited[nx]:
            end = nx
            break
        else:
            q.append(nx)
            visited[nx] = 1
    cur = start
    # 부분 사이클이 아닌 부분 제거
    while cur != end:
        out.add(cur)
        cur = board[cur]


tc = int(input())
for _ in range(tc):
    n = int(input())
    board = [0]+list(map(int, input().split()))
    visited = [0] * (n + 1)
    out = set()
    for i in range(1, n + 1):
        if not visited[i]:
            cycle(i)
    print(len(out))