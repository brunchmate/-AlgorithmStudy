# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from collections import defaultdict


def solution(info, query):
    answer = []
    infos = defaultdict(list)
    for i in info:
        i = i.split(" ")
        for a in [i[0], "-"]:
            for b in [i[1], "-"]:
                for c in [i[2], "-"]:
                    for d in [i[3], "-"]:
                        infos[a + b + c + d].append(int(i[4]))
    for k in infos.keys():
        infos[k].sort()
    for q in query:
        q = ''.join(q.split(" and "))
        q, score = q.split(" ")
        score = int(score)
        l, r = 0, len(infos[q])
        while l < r:
            m = (l + r) // 2
            if infos[q][m] >= score:
                r = m
            else:
                l = m + 1
        answer.append(len(infos[q]) - l)
    return answer
