# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 2
        n //= 2
    return answer
