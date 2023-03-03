def solution(N,stages):
    answer = []
    length = len(stages)
    for i in range(1,N+1):
        num = stages.count(i) 
        # ZeroDivisionError: division by zero
        if length == 0:
            answer.append((i,0))
        else:
            answer.append((i,num / length))
        length = length - num
    answer.sort(key = lambda x:(-x[1]))
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    return answer