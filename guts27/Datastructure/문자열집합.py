import sys
 
n, m = map(int, sys.stdin.readline().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline().strip())

cnt = 0
for _ in range(m):
    temp = sys.stdin.readline().strip()
    if temp in s:
        cnt += 1

print(cnt)
 
