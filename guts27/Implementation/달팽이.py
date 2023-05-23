import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
dx,dy = [0,1,0,-1],[1,0,-1,0]
graph = [[0 for _ in range(n)] for _ in range(n)]

answer = []
x,y = n//2, n//2
num = 1
length = 0

graph[x][y] = num

while True:
    for i in range(4):
        for _ in range(length):
            x += dx[i]
            y += dy[i]
            num += 1
            graph[x][y] = num
            if num == m:
                answer = [x+1,y+1]
    if x == 0 and y == 0:
        break
    x -= 1
    y -= 1
    length +=2
for i in range(n):
    print(*graph[i])
print(*answer)
    
    
    