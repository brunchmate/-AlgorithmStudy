# https://www.acmicpc.net/problem/10866
import sys

input = sys.stdin.readline

N = int(input())
q = [0] * N
front = 0 # 실제 front의 위치는 front 값의 +1에 있음
back = 0
size = 0
for _ in range(N):
    cmd = input().rstrip().split()
    if len(cmd) == 1:
        if cmd[0] == "pop_front":
            if size:
                front = (front + 1) % N
                print(q[front])
                size -= 1
            else:
                print(-1)
        elif cmd[0] == "pop_back":
            if size:
                print(q[back])
                back = (back - 1) % N
                size -= 1
            else:
                print(-1)
        elif cmd[0] == "size":
            print(size)
        elif cmd[0] == "empty":
            print(0 if size else 1)
        elif cmd[0] == "front":
            print(q[(front + 1) % N] if size else -1)
        elif cmd[0] == "back":
            print(q[back] if size else -1)
    else:
        if cmd[0] == "push_front":
            q[front] = cmd[1]
            front = (front - 1) % N
            size += 1
        elif cmd[0] == "push_back":
            back = (back + 1) % N
            q[back] = cmd[1]
            size += 1
