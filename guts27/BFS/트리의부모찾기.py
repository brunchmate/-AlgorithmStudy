#문제 꼼꼼하게 읽자
from collections import deque

def bfs(n,tree):
    queue = deque([1])
    parent = [0]*(n+1)
    
    while queue:
        num = queue.popleft()
        for i in tree[num]:
            if parent[i] == 0 and i != 1:
                parent[i] = num
                queue.append(i)

    for i in range(2,n+1):
        print(parent[i])
    
n = int(input())
tree = dict()
for i in range(1,n+1):
    tree[i] = []
for _ in range(n-1):
    x,y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

bfs(n,tree)
