# https://www.acmicpc.net/problem/1806
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = n + 1
left = 0
right = 0
cur = a[0]
while left <= right <= n:
    if cur >= s:
        if answer > right - left + 1:
            answer = right - left + 1
        cur -= a[left]
        left += 1
    else:
        right += 1
        if right < n:
            cur += a[right]
print(answer if answer <= n else 0)
