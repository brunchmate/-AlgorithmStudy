# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = [0, 0]
    done = set()
    prior = words[0][0]
    for i, w in enumerate(words):
        if w[0] != prior or w in done:
            answer = [i % n + 1, i // n + 1]
            break
        done.add(w)
        prior = w[-1]
    return answer
