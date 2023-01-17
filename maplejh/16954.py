# https://www.acmicpc.net/problem/16954
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 1), (0, 1), (-1, 0), (0, 0), (-1, -1), (0, -1), (1, 1), (1, 0), (1, -1)]


def dfs(sx, sy, depth):
    global answer
    if sx == 7 and sy == 0 or sy < depth:
        answer = 1
    if answer:
        return
    for dx, dy in d:
        nx = sx + dx
        ny = sy + dy
        if -1 < nx < 8 and -1 < ny < 8:
            if board[nx][ny] == '.':
                move()
                if board[nx][ny] == '.':
                    dfs(nx, ny, depth + 1)
                rev_move()


def move():
    tmp = []
    for i in range(8):
        board[i].rotate(1)
        tmp.append(board[i][0])
        board[i][0] = '.'
    mem.append(tmp)


def rev_move():
    rev_mem = mem.pop()
    for i in range(8):
        board[i].rotate(-1)
        board[i][-1] = rev_mem[i]


answer = 0
board = [deque(input().strip()) for _ in range(8)]
board = list(map(deque, zip(*board)))
mem = []
dfs(0, 7, 0)
print(answer)

# def bfs():
#     q = deque()
#     q.append((0, 7, 0))  # time,x,y
#     while q:
#         time, x, y = q.popleft()
#         for dx, dy in d:
#             nx = x + dx
#             ny = y + dy
#             if -1 < nx < 8 and -1 < ny < 8:
#                 if board[nx - time][ny] != '#' and board[nx - time - 1][ny] != "#": # time 이용하여 회전과 유사한 효과
#                     if nx <= time:  # time 보다 위에 있으면 모두 . 이니까 가능함
#                         return 1
#                     q.append((time + 1, nx, ny))
#     return 0
#
#
# board = [deque(input().strip()) for _ in range(8)]
# print(bfs())
