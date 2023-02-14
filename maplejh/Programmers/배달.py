# https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq


def solution(N, road, K):
    answer = 0

    board = [[10001] * N for _ in range(N)]
    for i in range(N):
        board[i][i] = 0
    for a, b, c in road:
        board[a - 1][b - 1] = min(board[a - 1][b - 1], c)
        board[b - 1][a - 1] = min(board[b - 1][a - 1], c)
    q = [(0, 0)]
    distance = [1e9] * N
    distance[0] = 0
    while q:
        cost, x = heapq.heappop(q)
        if distance[x] < cost:
            continue
        for i, nx in enumerate(board[x]):
            if 0 <= nx < 10001:
                if distance[i] > cost + nx:
                    distance[i] = cost + nx
                    heapq.heappush(q, (cost + nx, i))
    for d in distance:
        if d <= K:
            answer += 1
    return answer
