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


# union-find 개선
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)


def solution(k, room_number):
    def find(x):
        if parent[x]:
            parent[x] = find(parent[x])
            return parent[x]
        else:
            parent[x] = x + 1
            return x

    parent = defaultdict(int)
    answer = []
    for rn in room_number:
        answer.append(find(rn))
    return answer


# linked-list로도 가능
