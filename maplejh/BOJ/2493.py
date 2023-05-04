# https://www.acmicpc.net/problem/2493
import sys

input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

answer = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack:
        if tower[stack[-1]] > tower[i]:
            break
        idx = stack.pop()
        answer[idx] = i + 1
    stack.append(i)
print(*answer)
