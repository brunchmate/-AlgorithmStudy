# https://www.acmicpc.net/problem/15961
import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi.extend(sushi[:k])
l = 0
r = 0
cnt = defaultdict(int)
cnt[c] += 1
cnt[sushi[0]] += 1
kinds = len(cnt.keys())
ans = len(cnt.keys())
while l <= r:
    if r - l + 1 == k:
        if ans < kinds:
            ans = kinds
        cnt[sushi[l]] -= 1
        if cnt[sushi[l]] == 0:
            kinds -= 1
        l += 1
    else:
        r += 1
        if r == n+k:
            break
        cnt[sushi[r]] += 1
        if cnt[sushi[r]] == 1:
            kinds += 1
print(ans)
