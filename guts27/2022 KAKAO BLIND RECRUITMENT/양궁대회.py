def dfs(v, visited,count,info):
    global answer
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    
    if count == 0 or v == -1:     
        score_l = 0
        score_a = 0
        for i in range(10):
            if info[i] == 0 and visited[i]== 0:
                continue
            if info[i]>=visited[i]:
                score_a  =  score_a + arr[i]
            else:
                score_l = score_l + arr[i]

        if score_a < score_l and  answer[0] < score_l:
            if count != 0:
                visited[-1] = visited[-1]+ count
            answer = [score_l,visited[:]]
        return
    
    dfs(v-1, visited[:],count,info)
    
    if count > info[v]:
        visited[v] = info[v]+1
        dfs(v-1, visited[:],count-(info[v]+1),info)
        visited[v] = 0
    
        

def score(visited):
    num = 0
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    for i in range(len(visited)):
        if visited[i] != 0:
            num += arr[i]
    return num

def solution(n, info):
    global answer
    answer = [0,[0]]
    num = 0
    visited = [0 for _ in range(11)]
    dfs(10, visited,n,info)
        
    if len(answer[1]) == 1:
        return [-1]
    return answer[1]
