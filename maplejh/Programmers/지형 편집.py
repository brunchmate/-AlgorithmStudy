# https://school.programmers.co.kr/learn/courses/30/lessons/12984
from collections import defaultdict


def solution(land, P, Q):
    n = len(land)
    blocks = defaultdict(int)
    over_block = 0  # 기준 높이보다 더 있는 블록의 수
    h_block = n * n  # 기준 높이에 있는 블록의 수
    for l in land:
        for ll in l:
            if ll:
                blocks[ll] += 1
            else:
                h_block -= 1
            over_block += ll

    fill_block = 0  # 기준 높이를 채우기 위한 블록의 수
    answer = over_block * Q
    prior = 0  # 이전의 높이
    for flag in sorted(blocks.keys()):
        over_block -= h_block * (flag - prior)
        fill_block += (n * n - h_block) * (flag - prior)
        h_block -= blocks[flag]
        cost = fill_block * P + over_block * Q
        if answer > cost:
            answer = cost
        prior = flag
    return answer
