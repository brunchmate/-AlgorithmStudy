# https://www.acmicpc.net/problem/2630
import sys

input = sys.stdin.readline


def cnt(r, c, k): # r,c: 사각형의 시작점, k: 사각형의 크기
    if k == 1:
        if board[r][c]:
            return [0, 1]
        else:
            return [1, 0]
    res = [0, 0]
    # 사각형을 4등분한 작은 사각형들의 값을 구함
    k //= 2
    for i in range(2):
        for j in range(2):
            tmp = cnt(r + i * k, c + j * k, k)
            res[0] += tmp[0]
            res[1] += tmp[1]
    # 만약 작은 사각형에서 구한 값들이 모두 같으면 -> 하나의 큰 사각형으로 바꿈
    if not res[0]:
        res[1] = 1
    elif not res[1]:
        res[0] = 1
    return res


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = cnt(0, 0, N)
for a in ans:
    print(a)
