def dfs(visited,route,tickets,result):
    if result == length:
        answer.append(route[:])
        return 
    for i in range(len(tickets)):
        if visited[i] == True or route[-1] != tickets[i][0]:
            continue
        visited[i] = True
        route.append(tickets[i][1])
        dfs(visited,route,tickets,result+1)
        route.pop(-1)
        visited[i] = False
        
    
def solution(tickets):
    global answer,length
    length = len(tickets)
    answer = []
    visited = [False for i in range(len(tickets))]
    
    
    for i in range(len(tickets)):
        if tickets[i][0] ==  "ICN":
            route = []
            visited[i] = True
            route.append(tickets[i][0])
            route.append(tickets[i][1])
            dfs(visited,route,tickets,1)
            visited[i] = False
    answer.sort()
    return answer[0]
