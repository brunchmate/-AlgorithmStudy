import sys
input = sys.stdin.readline
INF = int(0xffffff) #무한을 의미하는 값으로 10억을 설정

#벨만 포드 알고리즘 구현 함수 
def bf(start):
#시작 노드에 대하여 초기화
    dist = [INF]*(n+1)
    dist[start]=0
    #전체 n번의 라운드를 반복
    for i in range(n):
        #매 반복마다 "모든 간선"을 확인하며
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]

            if dist[next_node]>dist[cur]+cost:
                dist[next_node] = dist[cur]+cost
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i==n-1:
                    return True
    return False

for _ in range(int(input())):
    n,m,w = map(int,input().split())
    edges=[]
    for _ in range(m):
        s,e,t= map(int,map(int,input().split()))
        edges.append([s,e,t])
        edges.append([e,s,t])

    for _ in range(w):
        s,e,t= map(int,map(int,input().split()))
        edges.append([s,e,-t])

    ncycle = bf(1) 

    print('YES' if ncycle else 'NO') 
