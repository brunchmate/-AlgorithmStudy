# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict


# 투포인터
def solution(gems):
    cnt = defaultdict(int)
    flag = len(set(gems))
    s = 0
    e = 0
    answer = [0, len(gems)]
    cnt[gems[0]] += 1
    while s <= e:
        if len(cnt) >= flag:
            if answer[1] - answer[0] > e - s:
                answer = [s + 1, e + 1]
            cnt[gems[s]] -= 1
            if cnt[gems[s]] == 0:
                del cnt[gems[s]]
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            cnt[gems[e]] += 1
    return answer
