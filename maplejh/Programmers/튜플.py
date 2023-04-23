# https://school.programmers.co.kr/learn/courses/30/lessons/64065
from collections import defaultdict


def solution(s):
    cnt = defaultdict(int)
    tuples = s[2:-2].split("},{")
    for t in tuples:
        for e in map(int, t.split(",")):
            cnt[e] += 1
    answer = [i[0] for i in sorted(cnt.items(), reverse=True, key=lambda x: x[1])]
    return answer


def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    prior = set()
    for i in sorted(s, key=lambda x: len(x)):
        i = set(map(int, i.split(",")))
        answer.append(*i ^ prior)
        prior = i

    return answer
