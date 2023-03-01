# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    alpha = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    def convert(s):
        q, r = divmod(s, n)
        if r in alpha.keys():
            r = alpha[r]
        if q:
            return convert(q) + str(r)
        else:
            return str(r)

    answer = ''
    for i in range(t * m):
        answer += convert(i)
    return answer[p - 1:t * m + p - 1][::m]
