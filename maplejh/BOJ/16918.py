# https://www.acmicpc.net/problem/16918
import sys

input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
ans = [["O"] * c for _ in range(r)]

if n == 1:
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                ans[i][j] = "."
elif n % 2:
    for i in range(r):
        for j in range(c):
            if board[i][j] == "O":
                ans[i][j] = "."
                for di, dj in d:
                    ni = i + di
                    nj = j + dj
                    if -1 < ni < r and -1 < nj < c:
                        ans[ni][nj] = "."
    if n % 4 == 1:
        bomb = set()
        for i in range(r):
            for j in range(c):
                if ans[i][j] == "O":
                    ans[i][j] = "."
                    bomb.add((i, j))
                    for di, dj in d:
                        ni = i + di
                        nj = j + dj
                        if -1 < ni < r and -1 < nj < c:
                            bomb.add((ni, nj))
                else:
                    ans[i][j] = "O"

        for bx, by in bomb:
            ans[bx][by] = "."

for a in ans:
    print("".join(a))
