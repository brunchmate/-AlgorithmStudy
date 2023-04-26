# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]
    l = 0
    r = 0
    res = sequence[0]

    while l <= r < n:
        if res < k:
            r += 1
            if r<n:
                res += sequence[r]
        else:
            if res == k:
                if answer[-1] - answer[0] > r - l:
                    answer = [l, r]
            res -= sequence[l]
            l += 1
    return answer
