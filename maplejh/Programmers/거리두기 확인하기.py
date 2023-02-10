# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque


def solution(places):
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def check(sx, sy):
        q = deque()
        q.append((0, sx, sy))
        visited = [[0] * 5 for _ in range(5)]
        visited[sx][sy] = 1
        while q:
            dist, x, y = q.popleft()
            if dist == 2:
                break
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < 5 and -1 < ny < 5:
                    if not visited[nx][ny] and place[nx][ny] != "X":
                        visited[nx][ny] = 1
                        q.append((dist + 1, nx, ny))
                        if dist < 2 and place[nx][ny] == "P":
                            return False
        return True

    answer = []
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not check(i, j):
                        answer.append(0)
                        break
            else:
                continue
            break
        else:
            answer.append(1)
    return answer
