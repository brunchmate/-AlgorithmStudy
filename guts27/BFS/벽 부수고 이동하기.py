from collections import deque
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((0,0,0))
    visited = [[[0]*m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = 1
    
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y, z = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[z][x][y]
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if 0 <= nx < n and 0<= ny <m: 
                # 벽이 아닌 경우
                if graph[nx][ny] == 0 and visited[z][nx][ny] == 0:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    queue.append((nx, ny,z))
                #벽이지만 아직 부순적 없을 경우
                elif graph[nx][ny] == 1 and z == 0:
                    visited[z+1][nx][ny] = visited[z][x][y] + 1
                    queue.append((nx, ny,z+1))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return -1
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(bfs(graph))
