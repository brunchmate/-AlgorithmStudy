# https://school.programmers.co.kr/learn/courses/30/lessons/133500
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def solution(n, lighthouse):
    def light(x):
        res = [0, 1]
        for nx in board[x]:
            if not visited[nx]:
                visited[nx] = 1
                tmp = light(nx)
                res[0] += tmp[1]
                res[1] += min(tmp)
        return res

    board = defaultdict(list)
    for a, b in lighthouse:
        board[a - 1].append(b - 1)
        board[b - 1].append(a - 1)
    visited = [0] * n
    visited[0] = 1
    return min(light(0))
