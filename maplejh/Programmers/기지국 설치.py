# https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math


def solution(n, stations, w):
    answer = 0
    start = 0
    r = 2 * w + 1
    stations.append(n + w + 1)
    for s in stations:
        end = s - w - 1
        if start < end:
            answer += math.ceil((end - start) / r)
        start = s + w
    return answer
