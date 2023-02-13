import heapq
INF = int(1e9)
                
def solution(N, road, K):
    answer = 0

    graph = [[] for i in range(N + 1)]
    visited = [INF] * (N+1)
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    q = []
    heapq.heappush(q,(0,1))
    visited[1] = 0
    while q:
        dist,now = heapq.heappop(q)
        if visited[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    #자기 자신도 가능
    for i in range(1,N+1):
        if visited[i] <= K:
            answer += 1
            
    return answer
