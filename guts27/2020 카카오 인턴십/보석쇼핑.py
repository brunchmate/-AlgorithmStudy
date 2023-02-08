#효율성 하나만 통과함
def solution(gems):
    answer = [0,len(gems)-1]
    gem_list = len(set(gems))
    end = 0
    
    for start in range(len(gems)):
        while end < len(gems):
            if start>end:
                end+=1
                continue
            if gem_list == len(set(gems[start:end+1])):
                if (answer[1]-answer[0]) > (end-start):
                    answer = [start,end]
                break
            end+=1
        
    answer = [answer[0]+1, answer[1]+1]
    return answer
