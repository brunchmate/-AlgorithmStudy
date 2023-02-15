# https://school.programmers.co.kr/learn/courses/30/lessons/49993
from collections import defaultdict


def solution(skill, skill_trees):
    answer = 0
    order = defaultdict(int)
    for i, s in enumerate(skill):
        order[s] = i + 1
    for skill_tree in skill_trees:
        cur = 0
        for s in skill_tree:
            if order[s] > cur:
                if order[s] == cur + 1:
                    cur += 1
                else:
                    break
        else:
            answer += 1

    return answer
