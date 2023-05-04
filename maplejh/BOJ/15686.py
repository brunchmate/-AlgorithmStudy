# https://www.acmicpc.net/problem/15686
import sys

input = sys.stdin.readline


def dfs(depth, idx):
    global answer
    if depth == m:
        answer = min(answer, sum(dist))
        return
    for x in range(idx, c):
        change = []
        # 치킨거리 계산/ 만약 더 크면
        for hi, h in enumerate(home):
            tmp = abs(chicken[x][0] - home[hi][0]) + abs(chicken[x][1] - home[hi][1])
            if tmp < dist[hi]:
                change.append((hi, dist[hi]))
                dist[hi] = tmp
        dfs(depth + 1, x + 1)
        for ci, cd in change:
            dist[ci] = cd

answer = 1e9
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))
dist = [10e9] * len(home)
c = len(chicken)
d = len(dist)
dfs(0, 0)
print(answer)
