from itertools import permutations
    
def solution(tickets):
    global answer
    answer = []

    v = [i for i in range(len(tickets))]
    _f = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            _f.append(i)
    
    for per in permutations(v,len(v)):
        route = []
        flag = 0
        nex = ""
        if per[0] not in _f:
            continue
        for p in per:
            if len(nex) == 0:
                route.append(tickets[p][0])
                route.append(tickets[p][1])
                nex = tickets[p][1]
                flag = 1
            else:
                if nex == tickets[p][0]:
                    route.append(tickets[p][1])
                    nex = tickets[p][1]
                else:
                    flag = 0
                    break
                    
        if flag == 1:
            answer.append(route)

    answer.sort()
    return answer[0]
