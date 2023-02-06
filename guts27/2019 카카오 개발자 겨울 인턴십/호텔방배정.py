# 효율성 통과 실패

def solution(k, room_number):
    answer = []
    # room = [[i] for i in range(k+1)]
    room = [False]*(k+1)
    for number in room_number:
        if room[number] == False:
            room[number] = True
            answer.append(number)
        else:
            r =  room.index(False,number)
            if r:
                room[r] = True
                answer.append(r)
    return answer
