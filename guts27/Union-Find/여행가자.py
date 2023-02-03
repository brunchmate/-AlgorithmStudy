n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
parent = [0]*(n)
load = list(map(int,input().split()))

for i in range(n):
    parent[i] = i
      
def parent_find(parent,x):
    if parent[x] != x:
        parent[x] = parent_find(parent,parent[x])
    return parent[x]

def union_find(parent,x,y):
    a = parent_find(parent,x)
    b = parent_find(parent,y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            union_find(parent, i,j)

root = parent[load[0]-1]
for i in load:
    if root != parent[i-1]:
        print('No')
        break
else:
    print('YES')
