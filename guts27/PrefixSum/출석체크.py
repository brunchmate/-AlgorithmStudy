import sys

n,k,q,m = map(int,sys.stdin.readline().split())
sleep = set(map(int,sys.stdin.readline().split()))
qr = set(map(int,sys.stdin.readline().split()))       
students = [0]*(n+3)

for q in (qr-sleep):
    for i in range(q,(n+3),q):
        if i in sleep:
            continue
        students[i] = True

ps = []
for i in range(3,n+3):
    if students[i] == True:
        students[i] = students[i-1]
    else:
        students[i] = students[i-1]+1
  
for _ in range(m):
    s, e= map(int,sys.stdin.readline().split())
    print(students[e]-students[s-1])
