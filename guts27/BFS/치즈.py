from collections import deque
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if 0 <= nx < n and 0<= ny <m and visited[nx][ny] == 0: 
                # 공기
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                #치즈
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
    return 
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
melt = 0
time = 0

while 1:
    temp = 0
    for i in range(n):
        for j in range(m):
            if graph [i][j] == 1:
                temp += 1
    if temp == 0:
        break
    else:
        bfs(graph)
        time = time+1
        melt = temp
        
print(time,melt)
