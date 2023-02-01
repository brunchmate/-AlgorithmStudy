# https://www.acmicpc.net/problem/2470
import sys

input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
board.sort()
start = 0
end = N - 1

x = start
y = end
ans = abs(board[0] + board[-1])
while start < end:
    cur = board[start] + board[end]
    if ans > abs(cur):
        x = start
        y = end
        ans = abs(cur)
    if cur < 0:
        start += 1
    elif cur > 0:
        end -= 1
    else:
        break

print(board[x], board[y])
