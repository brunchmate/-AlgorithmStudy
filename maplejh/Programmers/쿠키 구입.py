# https://school.programmers.co.kr/learn/courses/30/lessons/49995
def solution(cookie):
    answer = 0
    n = len(cookie)
    sums = [[0] * n for _ in range(n)]  # i열 부터 시작하는 누적합
    for i in range(n):
        sums[i][i] = cookie[i]
        for j in range(i + 1, n):
            sums[i][j] = sums[i][j - 1] + cookie[j]
    sums_transpose = list(zip(*sums))
    for x in range(1, n):
        answer = max(answer, max(set(sums_transpose[x - 1]) & set(sums[x])))
    return answer


# 미리 구할 필요없이 기준점 m을 기준으로 그때마다 누적합구하기
def solution(cookie):
    answer = 0
    n = len(cookie)
    for m in range(n):
        a = 0
        b = 0
        c = set()
        for i in range(m, -1, -1):
            a += cookie[i]
            c.add(a)
        for j in range(m + 1, n):
            b += cookie[j]
            if b in c:
                answer = max(answer, b)
    return answer
