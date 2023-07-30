# https://www.acmicpc.net/problem/20055
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
A = deque(map(int, input().split()))
robot = deque([0] * n)
stage = 0
zero = 0
while zero < k:
    stage += 1
    A.rotate(1)
    robot.rotate(1)
    robot[0] = 0
    robot[-1] = 0
    for i in range(n - 2, -1, -1):
        if robot[i]:
            if A[i+1] and not robot[i+1]:
                robot[i + 1] = 1
                robot[i] = 0
                A[i + 1] -= 1
                if not A[i + 1]:
                    zero += 1
    if A[0]:
        robot[0] = 1
        A[0] -= 1
        if not A[0]:
            zero += 1

print(stage)
