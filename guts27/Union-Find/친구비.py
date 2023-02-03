n,m,k= map(int,input().split())
money = [0]
money = money+ list(map(int,input().split()))
parent = [0]*(n+1)
cnt = 0

for i in range(n+1):
    parent[i] = i
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a==b:
        return
  ## 친구비를 기준으로 결정!!!!
    if money[a] < money[b]:
        parent[b] = a
    else:
        parent[a] = b
      
for _ in range(m):
    v,w = map(int,input().split())
    union_parent(parent,v,w)

for i,root in enumerate(parent):
    if i==root:
        cnt+=money[i]
      
if k >= cnt:
    print(cnt)
else:
    print("Oh no")
