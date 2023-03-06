# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = 1000
    n = len(s)
    for k in range(1, n // 2 + 2):
        compress = 0
        prior = ''
        cnt = 0
        for i in range(0, n + k, k):
            if prior == s[i:i + k]:
                cnt += 1
            else:
                compress += len(prior)
                if cnt > 1:
                    compress += len(str(cnt))
                prior = s[i:i + k]
                cnt = 1
        if answer > compress:
            answer = compress
    return answer
