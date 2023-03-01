# https://school.programmers.co.kr/learn/courses/30/lessons/17686
from collections import defaultdict


def solution(files):
    answer = []
    tmp = defaultdict(list)
    for idx, file in enumerate(files):
        head = ''
        number = ''
        for f in file:
            if f.isdigit():
                number += f
            else:
                if number:
                    break
                else:
                    head += f
        tmp[head.lower()].append((int(number), idx))
    for k in sorted(tmp.keys()):
        for v in sorted(tmp[k]):
            answer.append(files[v[1]])
    return answer
