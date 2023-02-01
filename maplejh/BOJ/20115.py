# https://www.acmicpc.net/problem/20115
import sys

input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))

board.sort()
ans = board[-1]
for i in range(N - 1):
    ans += board[i] / 2
print(ans)
