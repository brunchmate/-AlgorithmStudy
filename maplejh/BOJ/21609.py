# https://www.acmicpc.net/problem/21609
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(sx, sy):
    group = set()
    cur = board[sx][sy]
    group.add((sx, sy))
    q = deque()
    q.append((sx, sy))
    # 기준점, 전체개수, 빨강개수
    red = 0
    cnt = 1
    px = sx
    py = sy
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if (nx, ny) not in group:
                    group.add((nx, ny))
                    if board[nx][ny] == cur:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        cnt += 1
                        if px > nx:
                            px = nx
                            py = ny
                        elif px == nx and py > ny:
                            px = nx
                            py = ny
                    elif board[nx][ny] == 0:
                        q.append((nx, ny))
                        red += 1
                        cnt += 1
    return cnt, red, px, py


def find():
    group = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and board[x][y] > 0:
                visited[x][y] = 1
                group.append(bfs(x, y))
    group.sort(reverse=True)
    if not group or group[0][0] == 1:
        return 0
    else:
        bomb(group[0][2], group[0][3])
        gravity()
        counterclockwise90()
        gravity()
    return group[0][0] ** 2


def bomb(sx, sy):
    cur = board[sx][sy]
    group = set()
    group.add((sx, sy))
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        board[x][y] = -2
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if (nx, ny) not in group:
                    if board[nx][ny] == cur or board[nx][ny] == 0:
                        group.add((nx, ny))
                        q.append((nx, ny))


def gravity():
    for y in range(n):
        floor = n
        for x in range(n - 1, -1, -1):
            if board[x][y] == -2:
                continue
            elif board[x][y] == -1:
                floor = x
            else:
                tmp = board[x][y]
                board[x][y] = -2
                board[floor - 1][y] = tmp
                floor -= 1


def counterclockwise90():
    global board
    board = list(map(list, zip(*board)))[::-1]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = find()
    if flag:
        answer += flag
    else:
        break
print(answer)
