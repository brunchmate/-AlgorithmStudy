# https://www.acmicpc.net/problem/20057
import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
rd = {-1: [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1),
           (1, -1, 0.1), (0, -2, 0.05)],
      1: [(-1, -1, 0.01), (1, -1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, 1, 0.1),
          (1, 1, 0.1), (0, 2, 0.05)]}
cd = {-1: [(1, -1, 0.01), (1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02), (-1, -1, 0.1),
           (-1, 1, 0.1), (-2, 0, 0.05)],
      1: [(-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02), (1, -1, 0.1),
          (1, 1, 0.1), (2, 0, 0.05)]}
answer = 0

ci = n // 2
cj = n // 2
for flag in range(n + 1):
    d = (-1) ** flag
    for _ in range(flag):
        cj += d
        if cj < 0:
            break
        moved = 0
        for di, dj, da in rd[d]:
            ni = di + ci
            nj = dj + cj
            move = int(a[ci][cj] * da)
            moved += move
            if -1 < ni < n and -1 < nj < n:
                a[ni][nj] += move
            else:
                answer += move
        ni = ci
        nj = cj + d
        if -1 < ni < n and -1 < nj < n:
            a[ni][nj] += a[ci][cj] - moved
        else:
            answer += a[ci][cj] - moved
        a[ci][cj] = 0
    else:
        d = (-1) ** (flag + 1)
        for _ in range(flag):
            ci += d
            moved = 0
            for di, dj, da in cd[d]:
                ni = di + ci
                nj = dj + cj
                move = int(a[ci][cj] * da)
                moved += move
                if -1 < ni < n and -1 < nj < n:
                    a[ni][nj] += move
                else:
                    answer += move
            ni = ci + d
            nj = cj
            if -1 < ni < n and -1 < nj < n:
                a[ni][nj] += a[ci][cj] - moved
            else:
                answer += a[ci][cj] - moved
            a[ci][cj] = 0
print(answer)
