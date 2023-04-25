# https://www.acmicpc.net/problem/1463
import sys

input = sys.stdin.readline

x = int(input())
if x == 1:
    print(0)
elif 1 < x < 4:
    print(1)
else:
    dp = [0] * (x + 1)
    dp[2] = 1
    dp[3] = 1
    for i in range(4, x + 1):
        if not i % 6:
            dp[i] = min([dp[i // 3], dp[i // 2], dp[i - 1]]) + 1
        elif not i % 2:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        elif not i % 3:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1
    print(dp[-1])
