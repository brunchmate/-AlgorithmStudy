# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    uid = dict()
    for r in record:
        r = r.split(" ")
        if len(r) == 3:
            uid[r[1]] = r[2]
    for r in record:
        r = r.split(" ")
        if r[0] == "Enter":
            answer.append(uid[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(uid[r[1]] + "님이 나갔습니다.")
    return answer
