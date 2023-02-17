# https://school.programmers.co.kr/learn/courses/30/lessons/62050
from collections import deque, defaultdict

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def solution(land, height):
    def bfs(sx, sy, f):
        q = deque()
        q.append((sx, sy))
        groups[sx][sy] = f
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < n and -1 < ny < n:
                    if groups[nx][ny] > g:
                        if abs(land[nx][ny] - land[x][y]) <= height:
                            q.append((nx, ny))
                            groups[nx][ny] = f
                        else:
                            ladders[abs(land[nx][ny] - land[x][y])].add(tuple(sorted(((x, y), (nx, ny)))))

    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            visited[y] = x
        else:
            visited[x] = y

    def find(x):
        if visited[x] != x:
            visited[x]=find(visited[x])
        return visited[x]

    ladders = defaultdict(set)
    answer = 0
    n = len(land)
    g = 0
    groups = [[1e9] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if groups[i][j] > g:
                bfs(i, j, g)
                g += 1

    visited = [i for i in range(g)]
    for k in sorted(ladders.keys()):
        for l1, l2 in ladders[k]:
            g1 = groups[l1[0]][l2[1]]
            g2 = groups[l2[0]][l1[1]]
            if find(g1) != find(g2):
                union(g1, g2)
                answer+=k

    return answer