def dfs(v, visited,count,info):
    if count == 0 or v < 0:
        return visited

    for v in range(v,-1,-1):
            dfs(v-1, visited,count,info)
            
    if count > info[v]:
        visited[v] = info[v]+1
        count = count-(info[v]+1)
        for v in range(v,-1,-1):
            dfs(v-1, visited,count,info)
        
    return visited

def score(visited):
    num = 0
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    for i in range(len(visited)):
        if visited[i] != 0:
            num += arr[i]
    return num
def solution(n, info):
    answer = []
    num = 0
    score_a = score(info)
    for v in range(10, -1, -1):
        visited = [0 for _ in range(11)]
        visited = dfs(v,visited,n,info)
        score_l = score(visited)
        if num < score_l and score_a <score_l:
            answer = visited
    if len(answer) == 0:
        return [-1]
        
    return answer
