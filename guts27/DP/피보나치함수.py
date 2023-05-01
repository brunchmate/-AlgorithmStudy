def fibonacci(n):
    if n == 0:
        return [1,0]
    if n == 1:
        return [0,1]
    if graph[n] != [0,0]:
        return graph[n]
    graph[n] = [fibonacci(n-1)[i]+fibonacci(n-2)[i] for i in range(2)]
    return graph[n]

global zero, one
t= int(input())
graph = [[0,0] for _ in range(41)]
graph[0] = [1,0]
graph[1] = [0,1]
for _ in range(t):
    n = int(input())
    fibonacci(n)
    print(*graph[n])
