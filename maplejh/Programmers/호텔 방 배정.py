# https://school.programmers.co.kr/learn/courses/30/lessons/64063
import sys

sys.setrecursionlimit(10 ** 9)


# union-find
def solution(k, room_number):
    def union(x):
        x = find(x)
        parent[x] = x + 1

    def find(x):
        if parent.get(x, x) != x:
            parent[x] = find(parent[x])
        else:
            parent[x] = x
        return parent[x]

    parent = dict()
    answer = []
    for rn in room_number:
        if parent.get(rn, rn) != rn:
            nrn = parent[rn]
            if parent.get(nrn, nrn) != nrn:
                union(rn)
                answer.append(parent[nrn])
            else:
                answer.append(nrn)
                parent[nrn] = nrn + 1
        else:
            parent[rn] = rn + 1
            answer.append(rn)
    return answer
