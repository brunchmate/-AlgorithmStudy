# https://school.programmers.co.kr/learn/courses/30/lessons/17676
def solution(lines):
    answer = 0
    start = []
    end = []
    for l in lines:
        l = l.split(" ")
        hh, mm, ss = list(map(float, l[1].split(":")))
        e = ss + mm * 60 + hh * 3600
        s = e - float(l[2][:-1]) + 0.001
        end.append(e)
        start.append(s)
    n = len(lines)
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if start[j] - end[i] < 1:
                cnt += 1
        answer = max(answer, cnt)
    return answer
