import sys

n = int(sys.stdin.readline().strip())
level = [0]
level= level +list(map(int,sys.stdin.readline().split()))
q = int(sys.stdin.readline().strip())
ps = [0] * (n+1)
for i in range(1,n):
    if level[i] > level[i+1]:
        ps[i] = ps[i-1]+1
    else:
        ps[i] = ps[i-1] 
ps[n] = ps[n-1]
for _ in range(q):
    x,y = map(int,sys.stdin.readline().split())
    print(ps[y-1]-ps[x-1])
