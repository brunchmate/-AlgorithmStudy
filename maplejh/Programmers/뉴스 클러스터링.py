# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict


def solution(str1, str2):
    def make_set(strs):
        res = defaultdict(int)
        for i in range(1, len(strs)):
            if strs[i].isalpha() and strs[i - 1].isalpha():
                res[strs[i - 1:i + 1]] += 1
        return res

    a = make_set(str1.lower())
    b = make_set(str2.lower())
    union = 0
    intersection = 0
    for u in a.keys() | b.keys():
        union += max(a[u], b[u])
        intersection += min(a[u], b[u])
    answer = 65536
    if union:
        answer = int(answer * intersection / union)
    return answer
