# https://www.acmicpc.net/problem/3079
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
start = 0
end = max(T) * M
ans = end
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tk in T:
        total += mid // tk
    if total < M:
        start = mid + 1
    elif total >= M:
        end = mid - 1
        ans = mid
print(ans)
