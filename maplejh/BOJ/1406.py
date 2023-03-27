# https://www.acmicpc.net/problem/1406
from collections import deque
import sys

input = sys.stdin.readline

q = deque([0])
s = list(input().strip())
n = int(input())
q.extend(s)
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        q.append(cmd[1])
    else:
        if cmd[0] == "L":
            if q[-1] == 0:
                continue
            q.rotate(1)
        elif cmd[0] == "D":
            if q[0] == 0:
                continue
            q.rotate(-1)
        elif cmd[0] == "B":
            if q[-1] == 0:
                continue
            q.pop()
while q[0]:
    q.rotate()
q.popleft()
print(''.join(q))
