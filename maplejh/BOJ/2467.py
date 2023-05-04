# https://www.acmicpc.net/problem/2467
import sys

input = sys.stdin.readline

n = int(input())
feature = list(map(int, input().split()))

answer = 2000000000
a_s = 0
a_e = n - 1
s = 0
e = n - 1
while s < e:
    cur = feature[s] + feature[e]
    if answer > abs(cur):
        a_s = s
        a_e = e
        answer = abs(cur)
    if cur > 0:
        e -= 1
    elif cur < 0:
        s += 1
    else:
        break
print(feature[a_s], feature[a_e])
