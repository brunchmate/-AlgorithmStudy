# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []
    index = dict()
    for i in range(65, 91):
        index[chr(i)] = i - 64
    tmp = ''
    cur = 27
    for m in msg:
        if tmp + m in index.keys():
            tmp += m
            continue
        answer.append(index[tmp])
        index[tmp + m] = cur
        cur += 1
        tmp = m
    answer.append(index[tmp])
    return answer
