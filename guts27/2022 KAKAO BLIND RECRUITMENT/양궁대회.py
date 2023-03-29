def dfs(v, visited,count,info):
    global answer
    global score_a
    if v < 0:
        score_l = score(visited)
        if score_a < score_l and  answer[0]<= score_l:
            print(score_l,visited)
            answer = [score_l,visited[:]]
        return
            
    if count > info[v]:
        visited[v] = info[v]+1
        count = count-(info[v]+1)
        dfs(v-1, visited,count,info)
        visited[v] = 0
        count = count+(info[v]+1)
    
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
    global answer,score_a
    answer = [0,[0]]
    num = 0
    score_a = score(info)
    visited = [0 for _ in range(11)]
    dfs(10, visited,n,info)
        
    if answer[0] == 0:
        return [-1]
    return answer[1]
