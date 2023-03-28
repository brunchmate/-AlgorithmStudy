# https://www.acmicpc.net/problem/2512
import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())
req.sort()
start = m // n
end = req[-1]
while start <= end:
    mid = (start + end) // 2
    tmp = mid * n
    for r in req:
        if r < mid:
            tmp -= (mid - r)
        else:
            break
    if tmp > m:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)
