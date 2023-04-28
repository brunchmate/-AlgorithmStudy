import sys
sys.setrecursionlimit(2000)

def dfs(x,y):
    
    if visited[graph[x]] == False:
        visited[graph[x]] = True
        dfs(graph[x],y)

n = int(input())
for _ in range(n):
    t = int(input())
    answer = 0
    graph = [[] for _ in range(t+1)]
    visited = [False for _ in range(t+1)]
    for a,b in enumerate(list(map(int,input().split())),start = 1):
        graph[a] = b
    for i in range(1,t+1):
        if visited[i] == False:
            dfs(i,i)
            answer += 1
    print(answer)

numbers = [0] + list(map(int, input().split()))
visited = [True] + [False] * N #방문여부확인용
