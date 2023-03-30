# https://www.acmicpc.net/problem/1253
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = 0
for i in range(n):
    tmp = a[:i] + a[i + 1:]
    s = 0
    e = n - 2
    while s < e:
        cur = tmp[s] + tmp[e]
        if cur == a[i]:
            answer += 1
            break
        elif cur > a[i]:
            e -= 1
        else:
            s += 1
print(answer)
