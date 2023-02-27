# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        answer.append(format(a1 | a2, 'b').replace("1", "#").replace("0", " ").rjust(n, " "))
    return answer
