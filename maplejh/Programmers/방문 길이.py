# https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    answer = 0
    visited = [[[0, 0] for _ in range(11)] for _ in range(11)]
    cmd = {"L": 0, "D": 1, "R": 2, "U": 3}
    dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x = 5
    y = 5
    for d in dirs:
        nx = x + dd[cmd[d]][0]
        ny = y + dd[cmd[d]][1]
        if not (-1 < nx < 11 and -1 < ny < 11):
            continue
        if d == "D" or d == "L":
            if not visited[x][y][cmd[d]]:
                answer += 1
                visited[x][y][cmd[d]] = 1
        else:
            if not visited[nx][ny][cmd[d] - 2]:
                answer += 1
                visited[nx][ny][cmd[d] - 2] = 1
        x = nx
        y = ny

    return answer
