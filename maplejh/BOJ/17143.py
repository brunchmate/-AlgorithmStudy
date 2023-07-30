# https://www.acmicpc.net/problem/17143
import sys

input = sys.stdin.readline
d = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


def eat(y):
    for x in range(r):
        if board[x][y]:
            _, _, z = board[x][y]
            board[x][y] = []
            return z
    return 0


def move():
    res = [[[] for _ in range(c)] for _ in range(r)]
    fish = []
    for x in range(r):
        for y in range(c):
            if board[x][y]:
                ss, dd, zz = board[x][y]
                board[x][y] = []
                nx = d[dd][0] * ss + x
                ny = d[dd][1] * ss + y
                if not (-1 < nx < r and -1 < ny < c):
                    if dd == 1:
                        nx = -nx - 1
                        if (nx // (r - 1)) % 2:
                            nx = r - 2 - (nx % (r - 1))
                        else:
                            dd = 2
                            nx = 1 + (nx % (r - 1))
                    elif dd == 2:
                        nx = nx - r
                        if (nx // (r - 1)) % 2:
                            nx = 1 + (nx % (r - 1))
                        else:
                            dd = 1
                            nx = r - 2 - (nx % (r - 1))
                    elif dd == 3:
                        ny = ny - c
                        if (ny // (c - 1)) % 2:
                            ny = 1 + (ny % (c - 1))
                        else:
                            dd = 4
                            ny = c - 2 - (ny % (c - 1))
                    elif dd == 4:
                        ny = -ny - 1
                        if (ny // (c - 1)) % 2:
                            ny = c - 2 - (ny % (c - 1))
                        else:
                            dd = 3
                            ny = 1 + (ny % (c - 1))
                if res[nx][ny]:
                    if zz > res[nx][ny][-1]:
                        res[nx][ny] = [ss, dd, zz]
                else:
                    res[nx][ny] = [ss, dd, zz]
                    fish.append((nx, ny))

    for fx, fy in fish:
        board[fx][fy] = res[fx][fy]
    return res


r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    rr, cc, ss, dd, zz = map(int, input().split())
    board[rr - 1][cc - 1] = [ss, dd, zz]
answer = 0
for cur in range(c):
    answer += eat(cur)
    move()
print(answer)
