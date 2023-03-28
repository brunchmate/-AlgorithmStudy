# https://www.acmicpc.net/problem/13305
import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
total = sum(road)
answer = price[0] * total
prior = price[0]
for i in range(1, n - 1):
    total -= road[i - 1]
    if prior > price[i]:
        answer -= (prior - price[i]) * total
        prior = price[i]
print(answer)
