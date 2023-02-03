# https://www.acmicpc.net/problem/1976
import sys

input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
root = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            union(i, j)

# 모두 같은 조상인 경우에 가능
start = root[plan[0] - 1]
for p in plan:
    if start != root[p - 1]:
        print("NO")
        break
else:
    print("YES")
