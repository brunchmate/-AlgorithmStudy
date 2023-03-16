from itertools import combinations

def solution(orders, course):
    answer = []
    diction = {}
    for c in course:
        diction[c] = {}
    
    for order in orders:
        order = sorted(order)    
        for c in course:
            for per in combinations(order, c):
                per = list(per)
                per = "".join(per)
                
                if per not in diction[c]:
                    diction[c][per] = 1
                else:
                    num = diction[c][per]
                    diction[c][per] = num+1
    for c in course:
        if len(diction[c]) == 0:
            continue
        max_num = max(diction[c].values())
        if max_num == 1:
            continue
        for dic in diction[c].keys():
            if diction[c][dic] == max_num:
                answer.append(dic)
        
    return sorted(answer)
