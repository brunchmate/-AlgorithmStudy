# https://www.acmicpc.net/problem/14425
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    if input() in S:
        ans += 1
print(ans)
