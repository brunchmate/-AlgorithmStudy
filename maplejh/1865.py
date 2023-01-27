# https://www.acmicpc.net/problem/1865
import sys

input = sys.stdin.readline


def bellman_ford():
    dist = [0] * (N + 1)  # 모든 출발점들에 대해서 시작한다고 가정 -> 만약 모든 점에서 벨만포드를 돌리면 O(N^2M)시간복잡도
    for k in range(N):
        for i, j, c in board:
            if dist[i] != 1e9 and dist[j] > dist[i] + c:
                if k == N - 1:
                    return True
                dist[j] = dist[i] + c
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    board = []
    road = [[10000] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        if road[S][E] > T:
            road[S][E] = T
            road[E][S] = T
            board.append((S, E, T))
            board.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        board.append((S, E, -T))
    if bellman_ford():
        print("YES")
    else:
        print("NO")

# 설명: https://www.acmicpc.net/board/view/72995
