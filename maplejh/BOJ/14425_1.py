# https://www.acmicpc.net/problem/14425
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

root = {}
for _ in range(N):
    ss = input()
    node = root
    for s in ss:
        if s not in node:
            node[s] = {}
        node = node[s]
ans = 0
for _ in range(M):
    ss = input()
    node = root
    for s in ss:
        if s in node:
            node = node[s]
            continue
        else:
            break
    else:
        ans += 1
print(ans)
