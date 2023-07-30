# https://www.acmicpc.net/problem/20056
import sys

input = sys.stdin.readline


def fireball():
    res = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            while board[x][y]:
                cur = board[x][y].pop()
                nx = (x + cur[1] * d[cur[2]][0]) % n
                ny = (y + cur[1] * d[cur[2]][1]) % n
                res[nx][ny].append(cur)
    for x in range(n):
        for y in range(n):
            if len(res[x][y]) == 1:
                board[x][y] = res[x][y]
            elif len(res[x][y]) > 1:
                cnt = len(res[x][y])
                tmp = list(zip(*res[x][y]))
                w = sum(tmp[0]) // 5
                if not w:
                    continue
                s = sum(tmp[1]) // cnt
                flag = len(set(map(lambda fx: fx % 2, tmp[2]))) - 1
                for fd in [0, 2, 4, 6]:
                    board[x][y].append([w, s, fd + flag])


d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    rr, cc, mm, ss, dd = map(int, input().split())
    board[rr - 1][cc - 1].append([mm, ss, dd])

for _ in range(k):
    fireball()
answer = 0
for i in range(n):
    for j in range(n):
        while board[i][j]:
            answer += board[i][j].pop()[0]
print(answer)
