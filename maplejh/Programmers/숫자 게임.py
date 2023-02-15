# https://school.programmers.co.kr/learn/courses/30/lessons/12987
from collections import deque


def solution(A, B):
    answer = 0
    A = deque(sorted(A))
    B = deque(sorted(B))
    while A:
        if A[-1] >= B[-1]:
            A.pop()
            B.popleft()
        else:
            A.pop()
            B.pop()
            answer += 1
    return answer
