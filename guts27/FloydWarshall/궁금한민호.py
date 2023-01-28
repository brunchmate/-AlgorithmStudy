def floyd():
  
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if i == k or j == k or i==j:
                    continue

                if graph[i][j] == graph[i][k] + graph[k][i]:
                    graph[i][j] = 0
                  
                elif graph[i][j] > graph[i][k]+graph[k][j]:
                    return False
                
    res = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                res += graph[i][j]

    return res
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = floyd()

if not result:
    print(-1)
else:
    print(result)
