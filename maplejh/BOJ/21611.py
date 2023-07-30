# https://www.acmicpc.net/problem/21611
import sys

input = sys.stdin.readline
d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def magic(sx, sy, sd, ss):
    for _ in range(ss):
        sx += d[sd][0]
        sy += d[sd][1]
        if -1 < sx < n and -1 < sy < n:
            board[sx][sy] = 0
        else:
            break


def fill():
    f = -1
    for rx, ry in route:
        if board[rx][ry]:
            tmp = board[rx][ry]
            board[rx][ry] = 0
            board[route[f + 1][0]][route[f + 1][1]] = tmp
            f += 1
        else:
            continue


def explode():
    res = 0
    cnt = 0
    for ri in range(n ** 2):
        if not board[route[ri][0]][route[ri][1]]:
            break
        if cnt:
            if board[route[ri][0]][route[ri][1]] == board[route[ri - 1][0]][route[ri - 1][1]]:
                cnt += 1
            else:
                if cnt >= 4:
                    res += cnt * board[route[ri - 1][0]][route[ri - 1][1]]
                    for rk in range(1, cnt + 1):
                        board[route[ri - rk][0]][route[ri - rk][1]] = 0
                cnt = 1
        else:
            cnt += 1
    if cnt>=4:
        res += cnt * board[route[ri - 1][0]][route[ri - 1][1]]
        for rk in range(1, cnt + 1):
            board[route[ri - rk][0]][route[ri - rk][1]] = 0
    return res


def change():
    tmp = []
    for ri in range(n ** 2):
        if not board[route[ri][0]][route[ri][1]]:
            break
        if tmp:
            if tmp[-1] == board[route[ri][0]][route[ri][1]]:
                tmp[-2] += 1
            else:
                tmp.append(1)
                tmp.append(board[route[ri][0]][route[ri][1]])

        else:
            tmp.append(1)
            tmp.append(board[route[ri][0]][route[ri][1]])
        board[route[ri][0]][route[ri][1]] = 0
    for ri in range(min(len(tmp), n ** 2 - 1)):
        board[route[ri][0]][route[ri][1]] = tmp[ri]


n, m = map(int, input().split())
si = n // 2
sj = n // 2
route = []
for k in range(1, n + 1):
    for j in range(k):
        sj += (-1) ** k
        if sj == -1:
            break
        route.append((si, sj))
    else:
        for i in range(k):
            si += (-1) ** (k + 1)
            route.append((si, sj))
si = n // 2
sj = n // 2
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for _ in range(m):
    md, ms = map(int, input().split())
    magic(si, sj, md, ms)
    fill()
    while True:
        flag = explode()
        answer += flag
        if flag:
            fill()
        else:
            break
    change()
print(answer)
