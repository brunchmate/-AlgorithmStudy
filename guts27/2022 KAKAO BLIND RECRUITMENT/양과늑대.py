def dfs(now, sheep,wolf,next_arr,info,arr):
    global answer,visited

    if info[now] == 0:
        sheep += 1
    else:
        wolf += 1
        if sheep <= wolf:
            return    
    answer = max(answer,sheep)

    next_arr = next_arr + arr[now]
    for n in next_arr:
        # next_arr.remove(n)
        dfs(n, sheep,wolf, list(set(next_arr) - set([n])) ,info,arr)
    
    
    
def solution(info, edges):
    global answer,visited
    answer = 0
    arr = [[] for _ in range(len(info))]
    for x,y in edges:
        arr[x].append(y)
    dfs(0,0,0,[],info,arr)
    return answer


