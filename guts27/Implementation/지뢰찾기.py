n = int(input())
flag = False
dx,dy = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]
graph = [[0 for _ in range(n)] for _ in range(n)]
lm = []
for i in range(n):
    lm.append(list(input()))
for i in range(n):
    for j in range(n):
        if lm[i][j] == "*":
            graph[i][j] = "*"
            for x in range(8):
                nx = dx[x] + i
                ny = dy[x] + j
                if 0<=nx<n and 0<=ny<n and lm[nx][ny] == ".":
                    graph[nx][ny] += 1
graph2 = []
for i in range(n):
    graph2.append(list(input()))
for i in range(n):
    for j in range(n):
        if graph2[i][j] == ".":
            graph[i][j] = '.'
        elif graph2[i][j] == "x" and lm[i][j] == "*":
            flag = True
if flag:
    for i in range(n):
        for j in range(n):
            if lm[i][j] == "*":
                graph[i][j] = "*"
                
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()
