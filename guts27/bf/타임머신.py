import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
distance = [1e10]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))

def bf(start):
    distance[start] = 0
    for i in range(m):
        cur = graph[i][0]
        next_node = graph[i][1]
        cost = graph[i][2]
        if distance[cur] != 1e10 and distance[next_node] > distance[cur] + cost:
            distance[next_node] = distance[cur] + cost
            if i == n-1:
                return True
    return False

negative_cycle = bf(1)

if negative_cycle:
		print("-1")
else:
    for i in range(2,n+1):
        if distance[i] == 1e10:
            print("-1")
        else:
            print(distance[i])
