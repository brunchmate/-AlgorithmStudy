# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for ni in new_id:
        if ni.isdigit() or ni.isalpha() or ni in ["-", "_", "."]:
            answer += ni
    while ".." in answer:
        answer = answer.replace("..", ".")
    answer = answer.strip(".")
    if not answer:
        answer = "a"
    answer = answer[:15].strip(".").ljust(3, str(answer[-1]))
    return answer
