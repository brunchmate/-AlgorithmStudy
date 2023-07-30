import sys

input = sys.stdin.readline

d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cloud = {(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)}
for _ in range(m):
    md, ms = map(int, input().split())
    md -= 1
    cloud = set(((c[0] + d[md][0] * ms) % n, (c[1] + d[md][1] * ms) % n) for c in cloud)
    for cx, cy in cloud:
        a[cx][cy] += 1
    tmp = [[0] * n for _ in range(n)]
    for cx, cy in cloud:
        cnt = 0
        for di in [1, 3, 5, 7]:
            nx = cx + d[di][0]
            ny = cy + d[di][1]
            if -1 < nx < n and -1 < ny < n:
                if a[nx][ny]:
                    cnt += 1
        tmp[cx][cy] += cnt
    new_cloud = set()
    for x in range(n):
        for y in range(n):
            a[x][y] += tmp[x][y]
            if (x, y) not in cloud:
                if a[x][y] >= 2:
                    new_cloud.add((x, y))
                    a[x][y] -= 2
    cloud = new_cloud
answer = 0
for x in range(n):
    for y in range(n):
        answer += a[x][y]
print(answer)