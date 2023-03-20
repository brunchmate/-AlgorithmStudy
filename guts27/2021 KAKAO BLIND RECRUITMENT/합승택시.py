
def solution(n, s, a, b, fares):
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    answer = INF
    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for c in range(1, n + 1):
        for d in range(1, n + 1):
            if c == d:
                graph[c][d] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for c,d,e in fares:
        graph[c][d] = e
        graph[d][c] = e

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for c in range(1, n + 1):
            for d in range(1, n + 1):
                graph[c][d] = min(graph[c][d], graph[c][k] + graph[k][d])
    
    answer = min(answer,graph[s][a] + graph[s][b])
    answer = min(answer, graph[s][a] + graph[a][b])
    answer = min(answer,graph[s][b] + graph[b][a])
    
    for i in range(1,n+1):
        if i == s or i == b or i == a:
            continue
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
        
    return answer


