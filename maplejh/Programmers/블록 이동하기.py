# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque


def solution(board):
    n = len(board)
    visited = [[[10e9, 10e9] for _ in range(n)] for _ in range(n)]  # -,l 모양중에 왼쪽 위쪽에 있는 좌표
    visited[0][1][0] = 0
    q = deque()
    q.append((0, 0, 0, 1))
    d = {0: [[0, 1], [0, -1]], 1: [[1, 0], [-1, 0]]}
    while q:
        x1, y1, x2, y2 = q.popleft()
        flag = 0
        if x1 - x2:  # l모양
            flag = 1
        cost = visited[x2][y2][flag]
        # 한칸 이동
        for dx, dy in d[flag]:
            nx1 = dx + x1
            ny1 = dy + y1
            nx2 = dx + x2
            ny2 = dy + y2
            if -1 < nx1 < n and -1 < ny1 < n and -1 < nx2 < n and -1 < ny2 < n:
                if visited[nx2][ny2][flag] > cost + 1 and not board[nx1][ny1] and not board[nx2][ny2]:
                    visited[nx2][ny2][flag] = cost + 1
                    q.append((nx1, ny1, nx2, ny2))
        # 90도 회전/ 몸통전체 이동
        for dx, dy in d[abs(flag - 1)]:
            nx1 = dx + x1
            ny1 = dy + y1
            nx2 = dx + x2
            ny2 = dy + y2
            if -1 < nx1 < n and -1 < ny1 < n and -1 < nx2 < n and -1 < ny2 < n:
                if not board[nx1][ny1] and not board[nx2][ny2]:
                    if visited[nx2][ny2][flag] > cost + 1:
                        visited[nx2][ny2][flag] = cost + 1
                        q.append((nx1, ny1, nx2, ny2))
                    if dx == -1 or dy == -1:
                        if visited[x1][y1][abs(flag - 1)] > cost + 1:
                            visited[x1][y1][abs(flag - 1)] = cost + 1
                            q.append((nx1, ny1, x1, y1))
                        if visited[x2][y2][abs(flag - 1)] > cost + 1:
                            visited[x2][y2][abs(flag - 1)] = cost + 1
                            q.append((nx2, ny2, x2, y2))
                    elif dx == 1 or dy == 1:
                        if visited[nx1][ny1][abs(flag - 1)] > cost + 1:
                            visited[nx1][ny1][abs(flag - 1)] = cost + 1
                            q.append((x1, y1, nx1, ny1))
                        if visited[nx2][ny2][abs(flag - 1)] > cost + 1:
                            visited[nx2][ny2][abs(flag - 1)] = cost + 1
                            q.append((x2, y2, nx2, ny2))
    return min(visited[n-1][n-1])
