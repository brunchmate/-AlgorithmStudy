# https://www.acmicpc.net/problem/11725
import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 1))  # 부모, 자식
    while q:
        parent, child = q.popleft()
        root[child] = parent
        for grandchild in board[child]:
            if not root[grandchild]:
                q.append((child, grandchild))


N = int(input())
board = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
root = defaultdict(int)
bfs()
for i in range(2, N + 1):
    print(root[i])
