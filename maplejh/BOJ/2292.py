# https://www.acmicpc.net/problem/2292
import sys
input=sys.stdin.readline

n = int(input())
cnt = 1
start = 1
while start < n:
    start += 6 * cnt
    cnt += 1
print(cnt)
