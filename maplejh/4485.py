# https://www.acmicpc.net/problem/4485
import sys
import heapq

input = sys.stdin.readline
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
tc = 0
while True:
    n = int(input())
    if not n:
        break
    tc += 1
    board = [list(map(int, input().split())) for _ in range(n)]
    q = [(board[0][0], 0, 0)]
    visited = [[0] * n for _ in range(n)]
    visited[0][0]=1
    while q:
        c, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            break
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heapq.heappush(q, (c + board[nx][ny], nx, ny))
    print(f'Problem {tc}: {c}')
