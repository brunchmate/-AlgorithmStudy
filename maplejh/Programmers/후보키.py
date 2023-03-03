# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    candidate = set()
    trans = list(zip(*relation))
    nums = [i for i in range(len(trans))]
    for i in range(1, len(trans) + 1):
        for c in combinations(nums, i):
            # minimality
            for cand in candidate:
                if set(cand) & set(c) == set(cand):
                    break
            else:
                # uniqueness
                tmp = []
                for j in c:
                    tmp.append(trans[j])
                if len(relation) == len(set(zip(*tmp))):
                    candidate.add(c)
    return len(candidate)
