import heapq

dx,dy = [-1,0,1,0],[0,1,0,-1]
def dijkstra(start):
    q = []
    heapq.heappush(q,(graph[start][start],start,start))
    distance = [[1e9]*(n) for _ in range(n)]
    distance[start][start] = 0
    while q:
        dist,x,y = heapq.heappop(q)
        if x == n-1 and y== n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0> nx or nx >=n or 0>ny or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if distance[nx][ny]>cost: 
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
              
count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int,input().split()))
    distance = [[1e9]*(n) for _ in range(n)]
    dijkstra(0)
    count += 1
