def solution(record):
    answer = []
    names = {}
    for rec in record:
        rec = rec.split(' ')
        if rec[0] == 'Change':
            names[rec[1]] = rec[2]
        else:
            answer.append((rec[0], rec[1]))
            if rec[1] not in names.keys():
                names[rec[1]] = rec[2]
            elif rec[0] == "Enter" and rec[2] != names[rec[1]]:
                names[rec[1]] = rec[2]
    for i in range(len(answer)):
        if answer[i][0] == "Enter":
            answer[i] = names[answer[i][1]] + "님이 들어왔습니다."
        else:
            answer[i] = names[answer[i][1]] + "님이 나갔습니다."
    return answer