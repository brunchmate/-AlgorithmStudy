# https://www.acmicpc.net/problem/20438
import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
zzz = set(map(int, input().split()))
code = list(map(int, input().split()))
student = [1] * (N + 3)
for c in code:
    if c in zzz:
        continue
    for idx in range(c, N + 3, c):
        if idx in zzz:
            continue
        student[idx] = 0

prefix = [0] * (N + 3)
for idx in range(1, N + 3):
    prefix[idx] = student[idx] + prefix[idx - 1]

for _ in range(M):
    s, e = map(int, input().split())
    print(prefix[e] - prefix[s - 1])
