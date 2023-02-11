def dijkstra(start):
    q = []
    answer = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
def solution(n, start, end, roads, traps):
    answer = 0
    distance = [INF] * (n + 1)
    graph = [[] for i in range(n+1)
    # dist = [[False]*(n+1) for _ in range(n+1)]
    
    flag = 0
    
    for a,b,c in roads:
        # dist[a][b] = c
        # dist[b][a] = c
        graph[a].append((b,c))    
    
    dijkstra(start)


    
    
    
    
    return answer
