# https://www.acmicpc.net/problem/7562
import sys
from collections import deque

input = sys.stdin.readline

d = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, 1), (1, 2), (2, -1), (1, -2)]

tc = int(input())
for _ in range(tc):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    q = deque([(0, sx, sy)])
    visited = {(sx, sy)}
    while q:
        cnt, x, y = q.popleft()
        if x == ex and y == ey:
            print(cnt)
            break
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < l and -1 < ny < l:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((cnt + 1, nx, ny))
