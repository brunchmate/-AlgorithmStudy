# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    cur = [0] * (N + 2)  # 현재 진행중인 사람
    for s in stages:
        cur[s] += 1
    ppl = cur[N + 1]
    for i in range(N, 0, -1):
        ppl += cur[i]
        if ppl:
            answer.append((cur[i] / ppl, i))
        else:
            answer.append((0, i))
    answer = [c[1] for c in sorted(answer, key=lambda x: (-x[0], x[1]))]
    return answer
