# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace("10", "A")
    point = list(dartResult)
    for p in point:
        if p.isdigit():
            answer.append(int(p))
        if p == "A":
            answer.append(10)
        elif p == "D":
            answer[-1] = answer[-1] ** 2
        elif p == "T":
            answer[-1] = answer[-1] ** 3
        elif p == "*":
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif p == "#":
            answer[-1] *= -1
    return sum(answer)
