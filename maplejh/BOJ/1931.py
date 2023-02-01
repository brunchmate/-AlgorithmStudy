# https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    s, e = map(int, input().split())
    board.append((e, s))
board.sort()
end = 0
ans = 0
for e, s in board:
    if end > s:
        continue
    else:
        end = e
        ans += 1
print(ans)
