# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for c in course:
        candidates = defaultdict(int)
        for order in orders:
            for cand in combinations(sorted(order), c):
                candidates[cand] += 1
        cnt = 1
        if candidates:
            cnt = max(candidates.values())
        if cnt == 1:
            continue
        for k, v in candidates.items():
            if v == cnt:
                answer.append(''.join(k))
    return sorted(answer)
