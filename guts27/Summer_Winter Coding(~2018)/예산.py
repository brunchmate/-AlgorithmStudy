from itertools import combinations

def solution(d, budget):
    answer = len(d)
    d.sort()
    sum_num = sum(d)
    for i in range(len(d)-1,-1,-1):
        if sum_num > budget:
            sum_num -= d[i]
            answer -= 1
        else:
            break
    return answer