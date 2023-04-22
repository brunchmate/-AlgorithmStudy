def dfs(x):
    visited[x] = 1
    for y in graph[x]:
        if visited[y] == 1:
            continue
        dfs(y)
# if visited[y]==0:
	# dfs(y)
            
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)] # visited=[0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
		#graph[a]+=[b] # a에 b 연결
    #graph[b]+=[a] # b에 a 연결 -> 양방향
answer = 0
dfs(1)
for i in range(2,n+1):
    if visited[i] == 1:
        answer += 1
print(answer)
#print(sum(visited)-1)
